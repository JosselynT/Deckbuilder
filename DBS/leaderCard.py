from card import Card

class LeaderCard(Card):
    def __init__(self, type: str, name: str, number: str, colour: str, text: str, rarity: str,
    power: int, character: str, specialTrait: str, era: str, nameBack: str,
    textBack: str, powerBack: int, characterBack: str, specialTraitBack: str, eraBack: str):
        super().__init(type, name, number, colour, text, rarity)
        self.power = power
        self.character = character
        self.era = era
        self.nameBack = nameBack
        self.textBack = textBack
        self.powerBack = powerBack
        self.characterBack = characterBack
        self.specialTraitBack = specialTraitBack
        self.eraBack = eraBack
