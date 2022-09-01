from card import Card

class UnisonCard(Card):
    def __init__(self, type: str, name: str, number: str, colour: str, text: str, rarity: str,
    specifiedCost: str, power: int):
        super().__init__(type, name, number, colour, text, rarity)
        self.specifiedCost = specifiedCost
        self.power = power
