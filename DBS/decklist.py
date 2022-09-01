from sideDeck import SideDeck
from mainDeck import MainDeck
from zDeck import ZDeck
from leaderDeck import LeaderDeck

class Decklist():
    def __init__(self, leader: LeaderDeck, mainDeck: MainDeck, zDeck: ZDeck, sideDeck: SideDeck):
        self.leader = leader.number()
        self.mainDeck = mainDeck
        self.zDeck = zDeck
        self.sideDeck = sideDeck

    def isAllowed(self):
        if len(mainDeck) > mainDeck.maxSize or len(mainDeck) < mainDeck.minSize:
            return False
        if len(sideDeck) > sideDeck.maxSize or len(sideDeck) < sideDeck.minSize:
            return False
        if len(zDeck) > zDeck.maxSize or len(zDeck) < zDeck.minSize:
            return False
        return True
