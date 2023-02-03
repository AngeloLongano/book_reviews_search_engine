from typing import TypedDict


class DocumentModel(TypedDict):
    id_user: int
    name_user: str
    date: str
    title: str
    text: str
    score: float
    id_book: str
    price_book: str
    title_book: str
    negative_sentiment: float
    neutral_sentiment: float
    positive_sentiment: float

FIELDS = list(DocumentModel.__annotations__.keys())

def from_dirty_to_document_model(item) -> DocumentModel | None:
    if not is_valid(item) :
        return None
    else:
        return {
            "id_user": item["User_id"],
            "name_user": item["profileName"],
            "date": item["review/time"],
            "title": item["review/summary"],
            "text": item["review/text"],
            "score": float(item["review/score"]),

            "id_book": item["Id"],
            "price_book": float(item["Price"]),
            "title_book": item["Title"],
        }

def is_valid(item:dict)->bool :
    return item["Id"] != "" and item["User_id"] != "" and item["Title"] != "" and item["review/text"] != "" and item["review/score"] != "" and item["Price"] != ""