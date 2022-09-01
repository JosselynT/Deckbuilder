class Card():
    def __init__(self, type: str, name: str, number: str, colour: str, text: str,
     rarity: str):
        self.type = type
        self.name = name
        self.number = number
        self.colour = colour
        self.text = text
        self.rarity = rarity
        self.total = 4

    def setTotal(self, nb: int):
        self.total = nb

    def name(self):
        return self.name

    def number(self):
        return self.number

    def total(self):
        return self.total

    def banned(self):
        self.total = 0

    def limited(self):
        self.total = 1
