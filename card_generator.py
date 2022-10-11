import random

from datetime import datetime
from card_validator import CardValidator


class GetGenerate:
    def __init__(self, count=1, credit_type="Visa"):
        self.count = count
        self.credit_type = credit_type
        self.jdata = {"amex": ['34', '37'], "discover": ['65', '6011'],
                      "mastercard": ['51', '52', '53', '54', '55'], "visa": ['4']}
        self.info_card = {}
        self.ready_card = {}
        self.beautiful_card = None

    def cardInfo(self, card_list):
        for card_number in card_list:
            self.info_card.update({card_number: CardValidator(card_number).cardInfo()})

        return self.info_card

    def beautifulCard(self, card_list):
        if type([]) == type(card_list):
            self.beautiful_card = []
            for card_ids in card_list:
                out = []
                template_base = ""
                card_ids = str(card_ids)
                while card_ids:
                    out.append(card_ids[-4:])
                    card_ids = card_ids[:-4]
                    template_base = ' '.join(out[::-1])
                self.beautiful_card.append(template_base)
        elif type({}) == type(card_list):
            self.beautiful_card = {}
            for idList in card_list:
                card_ids = card_list[idList]['card']
                out = []
                template_base = ""
                while card_ids:
                    out.append(card_ids[-4:])
                    card_ids = card_ids[:-4]
                    template_base = ' '.join(out[::-1])
                jValue = {idList: {"card": template_base,
                                   "date": card_list[idList]['date'],
                                   "csv": card_list[idList]['csv']}}
                self.beautiful_card.update(jValue)
        return self.beautiful_card

    def getCard(self, beautiful_card=None, bank_info=None):
        if self.credit_type.lower() == "visa":
            for x in range(self.count):
                card_id = random.choice(self.jdata['visa'])
                if random.randint(0, 1):
                    while 1:
                        card_number = f"{card_id}{random.randint(111111111111, 999999999999)}"
                        if CardValidator(card_number).luhnValidator():
                            data_value = int(datetime.now().strftime("%y")) + random.randint(2, 6)
                            json_value = {x: {"card": f"{card_number}",
                                              "date": f"{random.randint(10, 28)}/{data_value}",
                                              "csv": random.randint(111, 999)}}
                            self.ready_card.update(json_value)
                            break
                else:
                    while 1:
                        card_number = f"{card_id}{random.randint(111111111111111, 999999999999999)}"
                        if CardValidator(card_number).luhnValidator():
                            data_value = int(datetime.now().strftime("%y")) + random.randint(2, 6)
                            json_value = {x: {"card": f"{card_number}",
                                              "date": f"{random.randint(10, 28)}/{data_value}",
                                              "csv": random.randint(111, 999)}}
                            self.ready_card.update(json_value)
                            break

        else:
            for x in range(self.count):
                card_id = random.choice(self.jdata[self.credit_type.lower()])
                if self.credit_type.lower() == "amex":
                    card_id = random.choice(self.jdata['amex'])
                    while 1:
                        card_number = f"{card_id}{random.randint(1111111111111, 9999999999999)}"
                        if CardValidator(card_number).luhnValidator():
                            data_value = int(datetime.now().strftime("%y")) + random.randint(2, 6)
                            json_value = {x: {"card": f"{card_number}",
                                              "date": f"{random.randint(10, 28)}/{data_value}",
                                              "csv": random.randint(111, 9999)}}
                            self.ready_card.update(json_value)
                            break
                else:
                    while 1:
                        card_number = f"{card_id}{random.randint(11111111111111, 99999999999999)}"
                        if CardValidator(card_number).luhnValidator():
                            data_value = int(datetime.now().strftime("%y")) + random.randint(2, 6)
                            json_value = {x: {"card": f"{card_number}",
                                              "date": f"{random.randint(10, 28)}/{data_value}",
                                              "csv": random.randint(111, 999)}}
                            self.ready_card.update(json_value)
                            break

        if beautiful_card:
            self.ready_card = GetGenerate().beautifulCard(self.ready_card)
        if bank_info:
            jsonInfoBank = {}
            for card_id in self.ready_card:
                ready_info = CardValidator(self.ready_card[card_id]['card']).cardInfo()
                jsonInfoBank.update({card_id: {"data": self.ready_card[card_id], "info": ready_info}})
            self.ready_card = jsonInfoBank
        return self.ready_card
