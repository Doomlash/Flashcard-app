from abc import ABC, abstractmethod
from pathlib import Path
import pickle


class LocalStorage(ABC):

    @abstractmethod
    def save_card(self, card):
        pass

    @abstractmethod
    def load_card(self, card):
        pass

    @abstractmethod
    def save_deck(self, deck):
        pass

    @abstractmethod
    def load_deck(self, deck):
        pass

class LocalStorageImpl(LocalStorage):

    def __init__(self):
        self.data_folder = Path(__file__).parent / "../data"
        self.card_folder = Path(__file__).parent / "../data/cards"
        self.deck_folder = Path(__file__).parent / "../data/decks"

    def save_card(self, card):
        outfile = open(self.card_folder / card.id, "wb")
        pickle.dump(card, outfile)
        outfile.close()

    def load_card(self, card):
        infile = open(self.card_folder / card.id, "rb")
        card = pickle.load(infile)
        infile.close()
        return card

    def save_deck(self, deck):
        pass

    def load_deck(self, deck):
        pass