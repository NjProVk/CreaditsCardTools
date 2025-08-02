# tests/test_card_generator.py
from card_generator.card_generator import CardGenerator
from card_generator.card_validator import CardValidator


def test_generate_single_card():
    """We check that the generator creates one valid map."""
    generator = CardGenerator("visa")
    cards = generator.generate(count=1)

    assert len(cards) == 1

    card_data = cards[0]
    assert "card" in card_data
    assert "expiry_date" in card_data
    assert "cvv" in card_data

    # The most important check: the generated map must be valid!
    validator = CardValidator(card_data["card"])
    assert validator.is_valid is True


def test_generate_multiple_cards():
    """Check that the generator creates the correct number of cards."""
    generator = CardGenerator("mastercard")
    cards = generator.generate(count=10)
    assert len(cards) == 10


def test_beautiful_format():
    """We check that the "beautiful" format adds spaces."""
    generator = CardGenerator("visa")
    cards = generator.generate(count=1, beautiful_format=True)

    card_number_formatted = cards[0]["card"]

    assert " " in card_number_formatted

    card_number_raw = card_number_formatted.replace(" ", "")

    assert len(card_number_raw) in [13, 16]


def test_include_bank_info():
    """
    Check that it is possible to add bank information during generation.
    This test will use the actual bin-list-data.csv file, so it is integrative.
    """
    generator = CardGenerator("visa")
    cards = generator.generate(count=1, include_bank_info=True)
    card_info = cards[0]["info"]
    assert isinstance(card_info, (dict, type(None)))
