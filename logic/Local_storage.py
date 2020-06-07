from abc import ABC, abstractmethod
from pathlib import Path
import pickle


class LocalStorage(ABC):
    data_folder = Path(__file__).parent / "../data"
    card_folder = Path(__file__).parent / "../data/cards"
    deck_folder = Path(__file__).parent / "../data/decks"

    @classmethod
    @abstractmethod
    def save_card(cls, card):
        pass

    @classmethod
    @abstractmethod
    def load_card(cls, card):
        pass

    @classmethod
    @abstractmethod
    def save_deck(cls, deck):
        pass

    @classmethod
    @abstractmethod
    def load_deck(cls, deck):
        pass

class LocalStorageImpl(LocalStorage):

    @classmethod
    def save_card(cls, card):
        outfile = open(cls.card_folder / card.name, "wb")

    @classmethod
    def load_card(cls, card):
        pass

    @classmethod
    def save_deck(cls, deck):
        pass

    @classmethod
    def load_deck(cls, deck):
        pass