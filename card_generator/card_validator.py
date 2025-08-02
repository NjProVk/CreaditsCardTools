"""
Credit Card Validation and BIN Lookup Module.

This module offers a robust `CardValidator` class to perform validation checks
on credit card numbers and retrieve information based on the Bank Identification
Number (BIN).

The validation process includes checking the number against the Luhn algorithm,
verifying its length, and matching its prefix to known payment card networks
(Visa, MasterCard, etc.).

A key feature of this module is its reliance on a local CSV database
(`binlist-data.csv`) for BIN lookups. This makes the process extremely fast,
reliable, and independent of rate-limited or unavailable external APIs. The module
is designed to gracefully handle the absence of the database file.

To function correctly, this module requires the `binlist-data.csv` file
to be present in the same directory.

Usage:
    validator = CardValidator("457173...0000")
    if validator.is_valid:
        print(f"Card Type: {validator.card_type}")
        info = validator.get_bin_info()
        if info:
            print(f"Bank: {info['bank']}")
"""

import csv
import re
from pathlib import Path
from typing import Any, Dict, Optional, cast

from .config import CARD_CONFIG


class CardValidator:
    """
    Checks card number validity, determines type and searches for
    information by BIN in local database. Works with current bin-list-data.csv format.
    """

    _bin_database: Optional[Dict[str, Dict[str, str]]] = None
    _db_path = Path(__file__).parent / "bin-list-data.csv"

    def __init__(self, card_number: str):
        self.card_number = re.sub(r"\D", "", str(card_number))
        self._card_type = None
        if CardValidator._bin_database is None:
            self._load_database()

    @classmethod
    def _load_database(cls):
        """
        Loads a BIN database from CSV, automatically defining headers.
        """
        cls._bin_database = {}
        try:
            with open(cls._db_path, mode="r", encoding="utf-8") as infile:
                reader = csv.DictReader(infile)
                for row_obj in reader:
                    row = cast(Dict[str, str], row_obj)

                    # DictReader itself uses the first line as headers
                    bin_code = row.get("BIN")
                    if bin_code:
                        cls._bin_database[bin_code] = {
                            "brand": row.get("Brand"),
                            "type": row.get("Type"),
                            "category": row.get("Category"),
                            "country": row.get("CountryName"),
                            "country_code": row.get("isoCode2"),
                            "bank": row.get("Issuer"),
                            "bank_url": row.get("IssuerUrl"),
                            "bank_phone": row.get("IssuerPhone"),
                        }
        except FileNotFoundError:
            print(f"Warning: BIN database file not found at {cls._db_path}")
            cls._bin_database = {}
        except Exception as e:
            print(f"Error loading BIN database: {e}")
            cls._bin_database = {}

    def is_luhn_valid(self) -> bool:
        """
        Verifies the card number using Luhn algorithm.
        Returns:
            bool: True if the number is valid according to Moon's algorithm.
        """
        if not self.card_number.isdigit():
            return False

        num = [int(x) for x in self.card_number]
        return sum(num[::-2] + [sum(divmod(2 * d, 10)) for d in num[-2::-2]]) % 10 == 0

    @property
    def card_type(self) -> str:
        """
        Defines and returns the card type ("visa", "mastercard", etc.).
        Returns "Unknown" if the type could not be determined.
        The result is cached.
        """
        if self._card_type is not None:
            return self._card_type
        card_len = len(self.card_number)

        for type_key, config in CARD_CONFIG.items():
            if card_len in config["lengths"]:

                for prefix in config["prefixes"]:
                    if self.card_number.startswith(prefix):

                        self._card_type = type_key
                        return self._card_type

        self._card_type = "Unknown"
        return self._card_type

    @property
    def is_valid(self) -> bool:
        """
        Full verification: the number must be valid according to the Moon algorithm and
            must belong to a known type.
        """
        return self.is_luhn_valid() and self.card_type != "Unknown"

    def get_bin_info(self) -> Optional[Dict[str, Any]]:
        """
        Searches for card information by its BIN (first 6 digits) in the local database.
        """
        if not self.card_number or not self._bin_database:
            return None

        bin_to_check = self.card_number[:6]
        return self._bin_database.get(bin_to_check)


__all__ = ["CardValidator"]
