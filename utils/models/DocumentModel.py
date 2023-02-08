from __future__ import annotations
from decimal import Decimal

from typing import TypedDict


class DocumentModel(TypedDict):
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


