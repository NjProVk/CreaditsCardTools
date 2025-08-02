# Card Toolkit

[![PyPI version](https://badge.fury.io/py/card_generator.svg)](https://badge.fury.io/py/card_generator)
[![CI Tests](https://github.com/NjProVk/CreaditsCardTools/actions/workflows/ci.yml/badge.svg)](https://github.com/NjProVk/CreaditsCardTools/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/pypi/l/card_generator)](https://opensource.org/licenses/MIT)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/card_generator)](https://pypi.org/project/card_generator/)

A powerful and dependency-free Python library to generate and validate credit card numbers. It uses a local, offline BIN database for fast and reliable bank and country lookups without needing API keys or internet access.

<details>
<summary><strong>Русская версия</strong></summary>

Мощная и не имеющая зависимостей Python-библиотека для генерации и валидации номеров кредитных карт. Использует локальную офлайн-базу данных BIN для быстрого и надежного определения банка и страны без необходимости в API-ключах или доступе в интернет.
</details>

---

## Key Features

-   **Generate Valid Cards**: Creates credit card numbers that pass the Luhn algorithm check for various schemes (Visa, MasterCard, Amex, Discover).
-   **Offline BIN Lookup**: Includes a local BIN database to retrieve card details like brand, type, country, and bank issuer.
-   **No Dependencies**: The core logic has zero external dependencies, making it lightweight and easy to integrate.
-   **No API Keys Required**: All lookups are performed locally, so you don't need to sign up for services or manage secret keys.
-   **Modern and Clean API**: Designed with clear, predictable methods and properties.
-   **Fully Typed**: Provides full type hinting for better autocompletion and static analysis.

## Installation

You can install the library from PyPI using `pip` or any other modern package manager like `uv`.

#### Using `pip`

```bash
# On Windows
py -m pip install card_generator

# On Linux/macOS
python3 -m pip install card_generator
```

#### Using `uv`

`uv` is an extremely fast, next-generation Python package installer.

```bash
# Install into your virtual environment (recommended)
uv pip install card_generator

# Or, if you need to install it system-wide (use with caution)
uv pip install --system card_generator
```

## Usage Examples

Here are some examples of how to use the library's main features.

### 1. Generating Credit Cards

Use the `CardGenerator` class to create one or more cards.

```python
from card_generator import CardGenerator

# Initialize a generator for MasterCard
mastercard_generator = CardGenerator("mastercard")

# Generate 3 standard cards
cards = mastercard_generator.generate(count=3)
print(cards)
```

**Example Output:**

```json
[
  {
    "card": "5486241234567890",
    "expiry_date": "07/28",
    "cvv": 451
  },
  {
    "card": "5179509876543210",
    "expiry_date": "11/29",
    "cvv": 812
  },
  {
    "card": "5543620011223344",
    "expiry_date": "02/27",
    "cvv": 123
  }
]
```

#### Generation with Options

You can generate cards with formatted numbers and include bank information.

```python
from card_generator import CardGenerator
import json

amex_generator = CardGenerator("amex")

# Generate 2 cards with formatting and bank info
pretty_cards = amex_generator.generate(
    count=2,
    beautiful_format=True,
    include_bank_info=True
)

print(json.dumps(pretty_cards, indent=2))
```

**Example Output:**

```json
[
  {
    "card": "3782 822463 10005",
    "expiry_date": "05/30",
    "cvv": 8812,
    "info": {
      "brand": "AMERICAN EXPRESS",
      "type": "CREDIT",
      "category": "",
      "country": "United States",
      "country_code": "US",
      "bank": "AMERICAN EXPRESS",
      "bank_url": "www.americanexpress.com",
      "bank_phone": ""
    }
  },
  {
    "card": "3412 345678 90127",
    "expiry_date": "12/28",
    "cvv": 1234,
    "info": null
  }
]
```
*(Note: `info` will be `null` if the generated BIN is not found in the local database.)*

---

### 2. Validating Credit Cards

Use the `CardValidator` class to check card numbers and get details.

```python
from card_generator import CardValidator

# A valid Visa card number
card_number = "4539920412345671"

# Initialize the validator
validator = CardValidator(card_number)

# --- Check Validity ---
print(f"Is Luhn valid? {validator.is_luhn_valid()}")

# --- Get Card Type ---
# This is a property, not a method
print(f"Card type: {validator.card_type}")

# --- Get All Available BIN Info ---
info = validator.get_bin_info()
print("BIN Info:")
print(info)
```

**Example Output:**

```
Is Luhn valid? True
Card type: visa
BIN Info:
{'brand': 'VISA', 'type': 'DEBIT', 'category': 'CLASSIC', 'country': 'Russian Federation', 'country_code': 'RU', 'bank': 'SBERBANK', 'bank_url': 'www.sberbank.ru', 'bank_phone': '+7-495-500-55-50'}
```

---

## Acknowledgements / Источник данных

This project utilizes the BIN list data provided by the `bin-list-data` project, which is maintained by venelinkochev and contributors. The data is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

-   **Source:** [github.com/venelinkochev/bin-list-data](https://github.com/venelinkochev/bin-list-data)

---

Этот проект использует данные из списка BIN, предоставленные проектом `bin-list-data` под руководством venelinkochev и его соавторов. Данные распространяются по лицензии [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/).

-   **Источник:** [github.com/venelinkochev/bin-list-data](https://github.com/venelinkochev/bin-list-data)
