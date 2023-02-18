import csv
import sys
from datetime import datetime
from decimal import Decimal

from utils.ManageReviewIndex import MangeReviewIndex
from utils.services.path_used_service import ANALYZED_DATA_PATH
from utils.services.time_decorator import long_time_function


@long_time_function
def create_index():
    """
    Funzione che salva la struttura degli indici nella cartella index
    """
    index_manager = MangeReviewIndex()

    with open(ANALYZED_DATA_PATH, newline='') as f:
        print("Creazione indice...")
        data = csv.DictReader(f)

        index_manager_functions = index_manager.writer_function()

        for index, item in enumerate(data):
            sys.stdout.write(f"\r\tDocumenti analizzati {index}")

            review = {
                **item,
                "score": int(float(item["score"])),
                "price_book": Decimal(item["price_book"]),
                "negative_sentiment": Decimal(item["negative_sentiment"]),
                "neutral_sentiment": Decimal(item["neutral_sentiment"]),
                "positive_sentiment": Decimal(item["positive_sentiment"]),

                "date": datetime.fromtimestamp(int(item["date"])),

            }
            # aggiunta del documento all'index
            index_manager_functions["add_document"](**review)
        index_manager_functions["save_document"]()
        print("\n")
