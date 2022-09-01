from card import Card

class ZLeaderCard(Card):
    def __init__(self, type: str, name: str, number: str, colour: str, text: str,
     rarity: str, power: int, character: str, specialTrait: str, era: str, zEnergyCost: int):
        super().__init__(type, name, number, colour, text, rarity)
        self.power = power
        self.character = character
        self.specialTrait = specialTrait
        self.era = era
        self.zEnergyCost = zEnergyCost
