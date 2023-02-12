from __future__ import annotations

from decimal import Decimal

from utils.models.DocumentModel import DocumentModel


class DocumentHelper:
    """
        Classe statica per gestire i documenti con modello standard
    """
    fields = list(DocumentModel.__annotations__.keys())

    @staticmethod
    def from_dirty(item: dict) -> DocumentModel | None:
        try:
            document = {
                "id_user": item["User_id"],
                "name_user": item["profileName"],
                "date": item["review/time"],
                "title": item["review/summary"],
                "text": item["review/text"],
                "score": int(float(item["review/score"])),

                "id_book": item["Id"],
                "price_book": Decimal(item["Price"]),
                "title_book": item["Title"],
            }
            return document
        except:
            return None
