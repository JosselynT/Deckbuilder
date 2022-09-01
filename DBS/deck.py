from card import Card

class Deck():
    def __init__(self, minSize: int, maxSize: int):
        self.list = {}
        self.minSize = minSize
        self.maxSize = maxSize

    def addCard(card: Card):
        self.list[card.name()] += 1 if self.list[card.name()] else self.list[card.name()] = 1

    def removeCard(card: Card):
        self.list[card.name()] -=1
        if self.list[card.name()] == 0:
            self.list.pop(card.name())
