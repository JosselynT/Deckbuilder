from card import card

class ExtraCard(Class):
    def __init__(self, type: str, name: str, number: str, colour: str, text: str, rarity: str,
    energyCost: int, specifiedCost: str):
        super().__init__(type, name, number, colour, text, rarity)
        self.energyCost = energyCost
