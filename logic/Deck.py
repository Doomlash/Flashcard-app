from abc import ABC, abstractmethod

class Deck(ABC):
    def __init__(self):
        super().__init__()
        self.name=None
        self._cards=None

class ListDeck(Deck):
    def __init__(self, name):
        super().__init__()
        self.name=name
        self._cards=[]

