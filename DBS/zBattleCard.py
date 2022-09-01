from card import Card

class ZBattleCard(Card):
    def __init__(self, type: str, name: str, number: str, colour: str, text: str, rarity: str,
    energyCost: int, specifiedCost: str, power: int, character: str,
    specialTrait: str, era: str, zEnergyCost: int):
        super().__init__(type, name, number, colour, text, rarity)
        self.energyCost = energyCost
        self.specifiedCost = specifiedCost
        self.power = power
        self.comboPower = comboPower
        self.comboCost = comboCost
        self.character = character
        self.specialTrait = specialTrait
        self.era = era
        self.zEnergyCost = zEnergyCost
