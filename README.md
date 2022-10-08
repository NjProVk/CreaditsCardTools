### CreditCardTools
Card generate, Card Validator, Credit card generate, Credit card validator

# English
#### Install:
<li><code>pip install requests</code></li>

<div align="center">Example</div>

##### Generator:
``` python
  from card_generator import GetGenerate
  GetGenerate(count=5, credit_type="MasterCard").getCard()
```
``` json
{"0": {"card": "52211052867270784", "data": "19/26", "csv": 176}, "1": {"card": "54457684365763339", "data": "25/24", "csv": 784}, "2": {"card": "54975537055351307", "data": "23/28", "csv": 315}, "3": {"card": "54825897202914387", "data": "10/25", "csv": 251}, "4": {"card": "53299342982928538", "data": "14/27", "csv": 774}}
```
>**GetGenerate** takes 2 arguments:
>  <li>count = Number of generations</li>
>  <li>credit_type = Card type (Visa, MasterCard, amex, discover)</li>
``` python
  from card_generator import GetGenerate
  GetGenerate(5, "MasterCard").getCard(beautiful_card=True)
```

``` json
{"0": {"card": "5427 9493 2235 6058", "data": "28/26", "csv": 264}, "1": {"card": "5562 7269 6515 5947", "data": "10/24", "csv": 874}, "2": {"card": "5334 6133 4766 5446", "data": "16/25", "csv": 704}, "3": {"card": "5442 8957 2666 9151", "data": "11/24", "csv": 747}, "4": {"card": "5486 9757 3211 5899", "data": "10/24", "csv": 428}}
```

``` python
  from card_generator import GetGenerate
  GetGenerate(5, "MasterCard").getCard(bank_info=True)
```

``` json
{"0": {"data": {"card": "5481022800389703", "data": "24/26", "csv": 387}, "info": {"type": "credit", "country": "Italy", "currency": "EUR", "short": "IT", "bank_name": "BANCA MONTE DEI PASCHI DI SIENA", "bank_phone": "577.294111", "bank_url": "www.mps.it"}}, "1": {"data": {"card": "5325911497824370", "data": "19/27", "csv": 305}, "info": {"type": "debit", "country": "United States of America", "currency": "USD", "short": "US", "bank_name": "FIDELITY INFORMATION SERVICES, INC.", "bank_phone": "888.323.0310", "bank_url": "www.fisglobal.com"}}, "2": {"data": {"card": "5179502864067664", "data": "16/26", "csv": 121}, "info": {"type": "credit", "country": "United States of America", "currency": "USD", "short": "US", "bank_name": "CITIBANK (SOUTH DAKOTA), N.A.", "bank_phone": "(605) 331-2626", "bank_url": "online.citibank.com"}}, "3": {"data": {"card": "5455820810161638", "data": "20/26", "csv": 217}, "info": {"country": "United States of America", "currency": "USD", "short": "US", "bank_name": "MELLON BANK, N.A.", "bank_phone": "(412) 236-3338"}}, "4": {"data": {"card": "5459496697261613", "data": "19/28", "csv": 917}, "info": {"type": "credit", "country": "Montenegro", "currency": "EUR", "short": "ME", "bank_name": "ATLAS BANKA A.D.", "bank_phone": "382 20 407 200", "bank_url": "www.atlasbanka.com"}}, "5": {"data": {"card": "5119641730184007", "data": "26/24", "csv": 647}, "info": {"type": "debit", "country": "United States of America", "currency": "USD", "short": "US", "bank_name": "COMPUTER SERVICES, INC.", "bank_phone": "(800) 545 4274", "bank_url": "www.csiweb.com"}}, "6": {"data": {"card": "5242172516811381", "data": "18/25", "csv": 950}, "info": {"type": "credit", "country": "Taiwan, Province of China[a]", "currency": "TWD", "short": "TW", "bank_name": "SUNNY BANK"}}, "7": {"data": {"card": "5468541498888178", "data": "26/27", "csv": 653}, "info": {"country": "United States of America", "currency": "USD", "short": "US", "bank_name": "PNC BANK, N.A.", "bank_phone": "888-762-2265", "bank_url": "www.pnc.com"}}, "8": {"data": {"card": "5543628362957384", "data": "26/26", "csv": 120}, "info": {"type": "credit", "country": "Russian Federation", "currency": "RUB", "short": "RU", "bank_name": "VTB BANK OJSC", "bank_phone": "(800) 100-24-24", "bank_url": "www.vtb.com"}}, "9": {"data": {"card": "5517546715162704", "data": "18/28", "csv": 199}, "info": {"type": "debit", "country": "United States of America", "currency": "USD", "short": "US", "bank_name": "STAR PROCESSING, INC.", "bank_phone": "+1 (416) 535-2424", "bank_url": "www.starprocessing.com"}}}
```

``` python
  from card_generator import GetGenerate
  GetGenerate(5, "MasterCard").getCard(bank_info=True, beautiful_card=True)
```

``` json
{0: {'data': {'card': '5537 6807 2093 2474', 'data': '23/24', 'csv': 612}, 'info': {'type': 'debit', 'country': 'United States of America', 'currency': 'USD', 'short': 'US', 'bank_name': 'FIDELITY INFORMATION SERVICES, INC.', 'bank_phone': '888.323.0310', 'bank_url': 'www.fisglobal.com'}}, 1: {'data': {'card': '5365 8857 3211 4428', 'data': '23/28', 'csv': 767}, 'info': {'type': 'credit', 'country': 'Brazil', 'currency': 'BRL', 'short': 'BR', 'bank_name': 'BANCO IBI S.A. BANCO MULTIPLO'}}, 2: {'data': {'card': '5148 6733 7784 8383', 'data': '22/24', 'csv': 795}, 'info': {'type': 'credit', 'country': 'United States of America', 'currency': 'USD', 'short': 'US', 'bank_name': 'US AIRWAYS DIVIDEND MILES', 'bank_phone': '800-428-4322', 'bank_url': 'www.usairways.com'}}, 3: {'data': {'card': '5343 8287 2801 9281', 'data': '18/25', 'csv': 547}, 'info': {'type': 'credit', 'country': 'United States of America', 'currency': 'USD', 'short': 'US'}}, 4: {'data': {'card': '5484 5588 5415 7733', 'data': '22/28', 'csv': 721}, 'info': {'type': 'credit', 'country': 'Russian Federation', 'currency': 'RUB', 'short': 'RU', 'bank_name': 'SAVINGS BANK OF THE RUSSIAN FEDERATION (SBERBANK)', 'bank_url': 'www.sbrf.ru'}}, 5: {'data': {'card': '5218 4647 0290 7234', 'data': '21/24', 'csv': 926}, 'info': {'type': 'credit', 'country': 'United States of America', 'currency': 'USD', 'short': 'US', 'bank_name': 'DIAMOND C.U.', 'bank_phone': '800.593.1000', 'bank_url': 'www.diamondcu.org'}}, 6: {'data': {'card': '5140 6522 8899 6802', 'data': '25/25', 'csv': 248}, 'info': {'type': 'credit', 'country': 'Russian Federation', 'currency': 'RUB', 'short': 'RU'}}, 7: {'data': {'card': '5392 8812 7130 5516', 'data': '22/27', 'csv': 953}, 'info': {'type': 'debit', 'country': 'Puerto Rico', 'currency': 'USD', 'short': 'PR'}}, 8: {'data': {'card': '5243 0860 8073 8821', 'data': '15/26', 'csv': 293}, 'info': {'type': 'debit', 'country': 'Costa Rica', 'currency': 'CRC', 'short': 'CR', 'bank_name': 'BANCO NACIONAL DE COSTA RICA', 'bank_phone': '(506)2211-2000', 'bank_url': 'www.bnonline.fi.cr'}}, 9: {'data': {'card': '5571 3570 6568 2231', 'data': '23/26', 'csv': 532}, 'info': {'type': 'credit', 'country': 'United States of America', 'currency': 'USD', 'short': 'US', 'bank_name': 'CITIBANK, N.A.', 'bank_phone': '1-800-374-9700', 'bank_url': 'online.citibank.com'}}}
```

>***getCard*** takes 2 arguments:
>  <li>beautiful_card = From xxxxxxxxxxxxxxxx to xxxx xxxx xxxx xxxx</li>
>  <li>bank_info = Card Information</li>

``` python
  from card_generator import GetGenerate
  GetGenerate().cardInfo(card_list=[5336897708041895, 5172409174953004])
```

``` json
{"5336897708041895": {"type": "credit", "country": "Russian Federation", "currency": "RUB", "short": "RU", "bank_name": "JSC RUSSIAN STANDARD BANK", "bank_phone": "7 7272 58 15 05", "bank_url": "www.rsb.ru"}, "5172409174953004": {"type": "credit", "country": "United States of America", "currency": "USD", "short": "US", "bank_name": "FIRST DATA CORPORATION", "bank_phone": "+1 888-477-3611", "bank_url": "www.firstdata.com"}}
```


>***card_list*** takes 1 arguments:
>  <li>card_list = Accepts a list</li>

``` python
  from card_generator import GetGenerate
  GetGenerate().beautifulCard(card_list=[5336897708041895, 5172409174953004])
```

``` list
['5336 8977 0804 1895', '5172 4091 7495 3004']
```

>***card_list*** takes 1 arguments:
>  <li>card_list = Accepts a list</li>

##### Validation:
``` python
  from card_validator import CardValidator
  CardValidator(card_number="5587896270574735").luhnValidator()
```
```
True
```
>**CardValidator** takes 1 arguments:
>  <li>card_number = Accepts card number</li>
>***luhnValidator***:
>  Checks via the moon algorithm</li>
``` python
  from card_validator import CardValidator
  CardValidator(card_number="5587896270574735").cardType()
```
```
MasterCard
```
>***cardType***:
>  What type of card</li>
``` python
  from card_validator import CardValidator
  CardValidator(card_number="5587896270574735").cardInfo()
```
``` json
{"type": null, "country": "United States of America", "currency": "USD", "short": "US"}
```
>***cardInfo***:
>  Shows map information</li>

# Russian
#### Установка:
<li><code>pip install requests</code></li>

<div align="center">Примеры</div>

##### Генератор:
``` python
  from card_generator import GetGenerate
  GetGenerate(count=5, credit_type="MasterCard")
```
``` json
{"0": {"card": "52211052867270784", "data": "19/26", "csv": 176}, "1": {"card": "54457684365763339", "data": "25/24", "csv": 784}, "2": {"card": "54975537055351307", "data": "23/28", "csv": 315}, "3": {"card": "54825897202914387", "data": "10/25", "csv": 251}, "4": {"card": "53299342982928538", "data": "14/27", "csv": 774}}
```
>**GetGenerate** принимает 2 аргумента:
>  <li>count = Число генераций</li>
>  <li>credit_type = Тип карты (Visa, MasterCard, amex, discover)</li>

``` python
  from card_generator import GetGenerate
  GetGenerate(5, "MasterCard").getCard(beautiful_card=True)
```

``` json
{"0": {"card": "5427 9493 2235 6058", "data": "28/26", "csv": 264}, "1": {"card": "5562 7269 6515 5947", "data": "10/24", "csv": 874}, "2": {"card": "5334 6133 4766 5446", "data": "16/25", "csv": 704}, "3": {"card": "5442 8957 2666 9151", "data": "11/24", "csv": 747}, "4": {"card": "5486 9757 3211 5899", "data": "10/24", "csv": 428}}
```

``` python
  from card_generator import GetGenerate
  GetGenerate(5, "MasterCard").getCard(bank_info=True)
```

``` json
{"0": {"data": {"card": "5481022800389703", "data": "24/26", "csv": 387}, "info": {"type": "credit", "country": "Italy", "currency": "EUR", "short": "IT", "bank_name": "BANCA MONTE DEI PASCHI DI SIENA", "bank_phone": "577.294111", "bank_url": "www.mps.it"}}, "1": {"data": {"card": "5325911497824370", "data": "19/27", "csv": 305}, "info": {"type": "debit", "country": "United States of America", "currency": "USD", "short": "US", "bank_name": "FIDELITY INFORMATION SERVICES, INC.", "bank_phone": "888.323.0310", "bank_url": "www.fisglobal.com"}}, "2": {"data": {"card": "5179502864067664", "data": "16/26", "csv": 121}, "info": {"type": "credit", "country": "United States of America", "currency": "USD", "short": "US", "bank_name": "CITIBANK (SOUTH DAKOTA), N.A.", "bank_phone": "(605) 331-2626", "bank_url": "online.citibank.com"}}, "3": {"data": {"card": "5455820810161638", "data": "20/26", "csv": 217}, "info": {"country": "United States of America", "currency": "USD", "short": "US", "bank_name": "MELLON BANK, N.A.", "bank_phone": "(412) 236-3338"}}, "4": {"data": {"card": "5459496697261613", "data": "19/28", "csv": 917}, "info": {"type": "credit", "country": "Montenegro", "currency": "EUR", "short": "ME", "bank_name": "ATLAS BANKA A.D.", "bank_phone": "382 20 407 200", "bank_url": "www.atlasbanka.com"}}, "5": {"data": {"card": "5119641730184007", "data": "26/24", "csv": 647}, "info": {"type": "debit", "country": "United States of America", "currency": "USD", "short": "US", "bank_name": "COMPUTER SERVICES, INC.", "bank_phone": "(800) 545 4274", "bank_url": "www.csiweb.com"}}, "6": {"data": {"card": "5242172516811381", "data": "18/25", "csv": 950}, "info": {"type": "credit", "country": "Taiwan, Province of China[a]", "currency": "TWD", "short": "TW", "bank_name": "SUNNY BANK"}}, "7": {"data": {"card": "5468541498888178", "data": "26/27", "csv": 653}, "info": {"country": "United States of America", "currency": "USD", "short": "US", "bank_name": "PNC BANK, N.A.", "bank_phone": "888-762-2265", "bank_url": "www.pnc.com"}}, "8": {"data": {"card": "5543628362957384", "data": "26/26", "csv": 120}, "info": {"type": "credit", "country": "Russian Federation", "currency": "RUB", "short": "RU", "bank_name": "VTB BANK OJSC", "bank_phone": "(800) 100-24-24", "bank_url": "www.vtb.com"}}, "9": {"data": {"card": "5517546715162704", "data": "18/28", "csv": 199}, "info": {"type": "debit", "country": "United States of America", "currency": "USD", "short": "US", "bank_name": "STAR PROCESSING, INC.", "bank_phone": "+1 (416) 535-2424", "bank_url": "www.starprocessing.com"}}}
```

``` python
  from card_generator import GetGenerate
  GetGenerate(5, "MasterCard").getCard(bank_info=True, beautiful_card=True)
```

``` json
{0: {'data': {'card': '5537 6807 2093 2474', 'data': '23/24', 'csv': 612}, 'info': {'type': 'debit', 'country': 'United States of America', 'currency': 'USD', 'short': 'US', 'bank_name': 'FIDELITY INFORMATION SERVICES, INC.', 'bank_phone': '888.323.0310', 'bank_url': 'www.fisglobal.com'}}, 1: {'data': {'card': '5365 8857 3211 4428', 'data': '23/28', 'csv': 767}, 'info': {'type': 'credit', 'country': 'Brazil', 'currency': 'BRL', 'short': 'BR', 'bank_name': 'BANCO IBI S.A. BANCO MULTIPLO'}}, 2: {'data': {'card': '5148 6733 7784 8383', 'data': '22/24', 'csv': 795}, 'info': {'type': 'credit', 'country': 'United States of America', 'currency': 'USD', 'short': 'US', 'bank_name': 'US AIRWAYS DIVIDEND MILES', 'bank_phone': '800-428-4322', 'bank_url': 'www.usairways.com'}}, 3: {'data': {'card': '5343 8287 2801 9281', 'data': '18/25', 'csv': 547}, 'info': {'type': 'credit', 'country': 'United States of America', 'currency': 'USD', 'short': 'US'}}, 4: {'data': {'card': '5484 5588 5415 7733', 'data': '22/28', 'csv': 721}, 'info': {'type': 'credit', 'country': 'Russian Federation', 'currency': 'RUB', 'short': 'RU', 'bank_name': 'SAVINGS BANK OF THE RUSSIAN FEDERATION (SBERBANK)', 'bank_url': 'www.sbrf.ru'}}, 5: {'data': {'card': '5218 4647 0290 7234', 'data': '21/24', 'csv': 926}, 'info': {'type': 'credit', 'country': 'United States of America', 'currency': 'USD', 'short': 'US', 'bank_name': 'DIAMOND C.U.', 'bank_phone': '800.593.1000', 'bank_url': 'www.diamondcu.org'}}, 6: {'data': {'card': '5140 6522 8899 6802', 'data': '25/25', 'csv': 248}, 'info': {'type': 'credit', 'country': 'Russian Federation', 'currency': 'RUB', 'short': 'RU'}}, 7: {'data': {'card': '5392 8812 7130 5516', 'data': '22/27', 'csv': 953}, 'info': {'type': 'debit', 'country': 'Puerto Rico', 'currency': 'USD', 'short': 'PR'}}, 8: {'data': {'card': '5243 0860 8073 8821', 'data': '15/26', 'csv': 293}, 'info': {'type': 'debit', 'country': 'Costa Rica', 'currency': 'CRC', 'short': 'CR', 'bank_name': 'BANCO NACIONAL DE COSTA RICA', 'bank_phone': '(506)2211-2000', 'bank_url': 'www.bnonline.fi.cr'}}, 9: {'data': {'card': '5571 3570 6568 2231', 'data': '23/26', 'csv': 532}, 'info': {'type': 'credit', 'country': 'United States of America', 'currency': 'USD', 'short': 'US', 'bank_name': 'CITIBANK, N.A.', 'bank_phone': '1-800-374-9700', 'bank_url': 'online.citibank.com'}}}
```

>***getCard*** принимает 2 аргумента:
>  <li>beautiful_card = Из xxxxxxxxxxxxxxxx к xxxx xxxx xxxx xxxx</li>
>  <li>bank_info = Информация по карте</li>

``` python
  from card_generator import GetGenerate
  GetGenerate().cardInfo(card_list=[5336897708041895, 5172409174953004])
```

``` json
{"5336897708041895": {"type": "credit", "country": "Russian Federation", "currency": "RUB", "short": "RU", "bank_name": "JSC RUSSIAN STANDARD BANK", "bank_phone": "7 7272 58 15 05", "bank_url": "www.rsb.ru"}, "5172409174953004": {"type": "credit", "country": "United States of America", "currency": "USD", "short": "US", "bank_name": "FIRST DATA CORPORATION", "bank_phone": "+1 888-477-3611", "bank_url": "www.firstdata.com"}}
```


>***card_list*** принимает 1 аргумент:
>  <li>card_list = Принимает список</li>

``` python
  from card_generator import GetGenerate
  GetGenerate().beautifulCard(card_list=[5336897708041895, 5172409174953004])
```

``` list
['5336 8977 0804 1895', '5172 4091 7495 3004']
```

>***card_list*** принимает 1 аргумент:
>  <li>card_list = Принимает список</li>

##### Валидация:
``` python
  from card_validator import CardValidator
  CardValidator(card_number="5587896270574735").luhnValidator()
```
```
True
```
>**CardValidator** принимает 1 аргумент:
>  <li>card_number = Принимает номер карты</li>
>***luhnValidator***:
>  Проверяет через алгоритм луны</li>
``` python
  from card_validator import CardValidator
  CardValidator(card_number="5587896270574735").cardType()
```
```
MasterCard
```
>***cardType***:
>  Какой тип карты</li>
``` python
  from card_validator import CardValidator
  CardValidator(card_number="5587896270574735").cardInfo()
```
``` json
{"type": null, "country": "United States of America", "currency": "USD", "short": "US"}
```
>***cardInfo***:
>  Показывает информацию по карте</li>
