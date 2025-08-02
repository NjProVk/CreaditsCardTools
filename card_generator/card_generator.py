"""
Credit Card Generation Module.

This module provides tools for generating valid, Luhn-compliant credit card numbers
for various payment networks such as Visa, MasterCard, American Express, and Discover.

The primary class, `CardGenerator`, creates one or more card data dictionaries,
each containing a card number, a randomly generated expiry date, and a CVV.
The generation process is data-driven, using a configuration dictionary that
defines the prefixes and length requirements for each card type.

Features:
- Generates numbers that pass the Luhn algorithm check.
- Supports multiple card schemes.
- Allows for "beautiful" formatting (e.g., "4929 8008 1234 5678").
- Can optionally enrich the generated card data with bank and country information
  by leveraging the `CardValidator` module to perform a local BIN lookup.

Usage:
    generator = CardGenerator("visa")
    cards = generator.generate(count=5, beautiful_format=True, include_bank_info=True)
"""

import secrets
from datetime import datetime
from typing import Any, Dict, List, Union

from .card_validator import CardValidator
from .config import CARD_CONFIG


class CardGenerator:
    """
    Generates valid credit card numbers of various payment systems.
    """

    def __init__(self, card_type: str = "visa"):
        """
        Initialises the generator for the specified card type.

        Args:
            card_type (str): The card type (e.g. "visa", "mastercard"). Default is "visa".

        Raises:
            ValueError: if an unsupported card type is specified.
        """
        self.card_type = card_type.lower()
        if self.card_type not in CARD_CONFIG:
            raise ValueError(
                f"Неподдерживаемый тип карты: '{card_type}'. "
                f"Доступные типы: {list(CARD_CONFIG.keys())}"
            )
        self.config = CARD_CONFIG[self.card_type]

    @staticmethod
    def format_card_number(card_number: str) -> str:
        """
        Formats the card number into groups of 4 digits.
        Example: "1234567812345678" -> "1234 5678 1234 5678".
        """
        return " ".join([card_number[i : i + 4] for i in range(0, len(card_number), 4)])

    def _generate_single_card(self) -> Dict[str, Union[str, int]]:
        """Generates a single valid card in the form of a dictionary."""
        prefix = secrets.choice(self.config["prefixes"])
        length = secrets.choice(self.config["lengths"])

        while True:
            random_part_len = length - len(prefix)
            random_digits = [str(secrets.randbelow(10)) for _ in range(random_part_len)]
            card_number = prefix + "".join(random_digits)

            # Check by Luhn algorithm. If invalid, generate again.
            if CardValidator(card_number).is_luhn_valid():
                break

        # Generation of expiry date and CVV
        current_year = int(datetime.now().strftime("%y"))
        exp_year = current_year + secrets.randbelow(5) + 2  # randint(2,6)
        exp_month = secrets.randbelow(12) + 1  # randint(1,12)

        # Amex has a 4-digit CVV, the others have a 3-digit CVV
        cvv_length = 4 if self.card_type == "amex" else 3
        cvv = secrets.randbelow(10**cvv_length - 10 ** (cvv_length - 1)) + 10 ** (
            cvv_length - 1
        )  # randint(100,900)

        return {
            "card": card_number,
            "expiry_date": f"{exp_month:02d}/{exp_year}",
            "cvv": cvv,
        }

    def generate(
        self,
        count: int = 1,
        beautiful_format: bool = False,
        include_bank_info: bool = False,
    ) -> List[Dict[str, Any]]:
        """
        Generates a list of credit cards.

        Args:
            count (int): The number of maps to generate.
            beautiful_format (bool): If True, the card number will be formatted with spaces.
            include_bank_info (bool): If True, bank information will be added to the result.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries, where each dictionary represents a map.
        """
        generated_cards: List[Dict[str, Any]] = [
            self._generate_single_card() for _ in range(count)
        ]

        if include_bank_info:
            for card in generated_cards:
                card["info"] = CardValidator(card["card"]).get_bin_info()

        if beautiful_format:
            for card in generated_cards:
                card["card"] = self.format_card_number(card["card"])

        return generated_cards
