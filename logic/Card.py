from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self):
        super().__init__()
        self.deck = None
        self.name = None
        self.question = None
        self.answer = None
        self.id = self.generate_id()
    @abstractmethod
    def generate_id(self):
        pass

class TextCard(Card):

    def generate_id(self):
        return self.deck.name+'-'+self.name+
