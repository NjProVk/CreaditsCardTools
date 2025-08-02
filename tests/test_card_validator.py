# tests/test_card_validator.py
import pytest

from card_generator.card_validator import CardValidator

# --- Validation and type definition tests ---


def test_valid_visa_luhn_check():
    """Verifying that a known valid Visa card passes the luhn check."""
    validator = CardValidator("4539920412345671")
    assert validator.is_luhn_valid() is True


def test_invalid_luhn_check():
    """Check that a card with an invalid checksum does not pass validation."""
    validator = CardValidator("4539920412345678")
    assert validator.is_luhn_valid() is False


def test_identify_card_type():
    """Check if the card types are defined correctly."""
    assert CardValidator("4929800812345678").card_type == "visa"
    assert CardValidator("5469123400000000").card_type == "mastercard"
    assert CardValidator("378282246310005").card_type == "amex"
    assert CardValidator("1234567890123").card_type == "Unknown"


def test_full_validation():
    """We test the is_valid property that combines luhn and type."""
    # Valid by the luhn and a known type
    assert CardValidator("4539920412345671").is_valid is True
    # Invalid by luhn
    assert CardValidator("4539920412345678").is_valid is False
    # Valid by luhn, but unknown type
    assert CardValidator("1111222233334444").is_valid is False


# --- BIN search tests using a dummy database ---


@pytest.fixture
def mock_db(tmp_path, monkeypatch):
    """
    This test will use the actual bin-list-data.csv file, so it is integrative.
    """
    db_content = (
        "BIN,Brand,Type,Category,Issuer,IssuerPhone,IssuerUrl,isoCode2,isoCode3,CountryName\n"
        '555555,MASTERCARD,CREDIT,,TEST BANK,,,US,USA,"United States"\n'
    )
    db_path = tmp_path / "test-bin-data.csv"
    db_path.write_text(db_content, encoding="utf-8")

    CardValidator._db_path = db_path
    CardValidator._bin_database = None


def test_get_bin_info_found(mock_db):
    """Verifying that the information is in our dummy database."""
    validator = CardValidator("5555551234567890")
    info = validator.get_bin_info()
    assert info is not None
    assert info["bank"] == "TEST BANK"
    assert info["country_code"] == "US"


def test_get_bin_info_not_found(mock_db):
    """Check that None is returned for a BIN that is not in the database."""
    validator = CardValidator("1111110000000000")
    info = validator.get_bin_info()
    assert info is None
