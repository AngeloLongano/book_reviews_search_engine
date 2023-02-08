from __future__ import annotations

from decimal import Decimal

from utils.models.DocumentModel import DocumentModel


class DocumentHelper:
    fields = list(DocumentModel.__annotations__.keys())

    @classmethod
    def from_dirty(cls, item: dict) -> DocumentModel | None:
        try:
            document = {
                "id_user": item["User_id"],
                "name_user": item["profileName"],
                "date": item["review/time"],
                "title": item["review/summary"],
                "text": item["review/text"],
                "score": int(float(item["review/score"])),  # TODO: Provare a togliere il float

                "id_book": item["Id"],
                "price_book": Decimal(item["Price"]),
                "title_book": item["Title"],
            }
            return document
        except:
            return None
