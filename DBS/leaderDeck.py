from deck import Deck

class LeaderDeck(Deck):
    def __init__(self):
        super().__init__(1, 1)

    def addCard(card: Card):
        self.list = {}
        self.list[card.number()] = 1
