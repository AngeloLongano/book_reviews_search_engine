from abc import ABC, abstractmethod
from typing import Callable

from utils.models.DocumentModel import DocumentModel


class ManageIndexAbstract(ABC):
    """
    Classe astratta per definire il comportamento di un index manager
    """
    @abstractmethod
    def search_index(self, query: str, field: str, sentiment: str, max_results: int, reversed_sort: int, sort_by: str):
        pass

    @abstractmethod
    def writer_function(self) -> {"add_document": Callable[[DocumentModel], None], "save_document": Callable[[], None]}:
        pass

    @abstractmethod
    def suggest_words(self, mistyped_word: str):
        pass

    @abstractmethod
    def correct_query(self, query:str):
        pass
