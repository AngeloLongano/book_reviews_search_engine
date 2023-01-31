from typing import TypedDict

"""
Modellazione dei dati
"""


class DocumentModel(TypedDict):
    id_document: int
    title: str
    description: str
    category: str

class SentimentAnalysisModel(TypedDict):
    id_document: int
    negative_score: float
    neutral_score: float
    positive_score: float
