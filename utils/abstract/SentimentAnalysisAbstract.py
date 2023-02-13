from abc import ABC, abstractmethod


class SentimentAnalysisAbstract(ABC):
    """
    Classe astratta per definire il comportamento di un sentiment analyzer
    """
    @abstractmethod
    def sentiment(self, text: str) -> {"negative": float, "neutral": float, "positive": float}:
        pass
