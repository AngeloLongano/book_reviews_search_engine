from decimal import Decimal
from typing import TypedDict


class DocumentModel(TypedDict):
    """
    Assegnazione ad ogni variabile del modello utilizzata ad una tipologia specifica
    """
    id_user: int
    name_user: str
    date: str
    title: str
    text: str
    score: int
    id_book: str
    price_book: Decimal
    title_book: str
    negative_sentiment: Decimal
    neutral_sentiment: Decimal
    positive_sentiment: Decimal


