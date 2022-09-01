from card import Card

class Deck():
    def __init__(self, minSize: int, maxSize: int):
        self.list = {}
        self.minSize = minSize
        self.maxSize = maxSize

    def addCard(card: Card):
        if self.list[card.number()]:
            if self.list[card.number()]+1 < card.total():
                self.list[card.number()] += 1
        else:
            self.list[card.number()] = 1

    def removeCard(card: Card):
        self.list[card.number()] -=1
        if self.list[card.number()] == 0:
            self.list.pop(card.number())

    def selectCard(card: Card):
        return self.list[card.number()]
