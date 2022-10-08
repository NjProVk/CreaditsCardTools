import requests


class CardValidator:
    def __init__(self, card_number):
        self.card_number = str(card_number)
        self.len_card = len(str(card_number))
        self.luhn_valid = None
        self.card_info = {}
        self.jdata = {'AMEX': ['34', '37'], 'Discover': ['65', '6011'],
                      'MasterCard': ['51', '52', '53', '54', '55'], 'Visa': ['4']}
        self.type_card = 'Unknown'

    def luhnValidator(self):
        double = 0
        total = 0

        digits = str(self.card_number)

        for i in range(len(digits) - 1, -1, -1):
            for c in str((double + 1) * int(digits[i])):
                total += int(c)
            double = (double + 1) % 2

        self.luhn_valid = (total % 10) == 0
        return self.luhn_valid

    def cardType(self):
        # AMEX
        if self.len_card == 15 and self.card_number[:2] in self.jdata['AMEX']:
            self.type_card = 'AMEX'

        # MasterCard, Visa, and Discover
        elif self.len_card == 16:
            # MasterCard
            if self.card_number[:2] in self.jdata['MasterCard']:
                self.type_card = 'MasterCard'

            # Discover
            elif self.card_number[:2] in self.jdata['Discover'] or self.card_number[:4] in self.jdata['Discover']:
                self.type_card = 'Discover'

            # Visa
            elif self.card_number[:1] in self.jdata['Visa']:
                self.type_card = 'Visa'

        # VISA
        elif self.len_card == 13 and self.card_number[:1] in self.jdata['Visa']:
            self.type_card = 'Visa'

        return self.type_card

    def cardInfo(self):
        req = requests.get(f"https://lookup.binlist.net/{self.card_number.replace(' ', '')[:6]}")
        if req.status_code == 200:
            j_req = req.json()
            try:
                self.card_info.update({"type": j_req['type']})
            except:
                ...
            self.card_info.update({
                "country": j_req['country']['name'],
                "currency": j_req['country']['currency'],
                "short": j_req['country']['alpha2'],
            })
            if j_req['bank']:
                for ids in ['name', 'phone', 'url']:
                    try:
                        self.card_info.update({
                            f"bank_{ids}": j_req['bank'][ids],
                        })
                    except:
                        ...
        else:
            return None

        return self.card_info
