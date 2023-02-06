import csv
import os
import sys
from datetime import datetime

from utils.ManageReviewIndex import MangeReviewIndex

# path per il file books_ratings.csv
data_path = os.getcwd() + "/processed_data/books_rating_with_sentimental.csv"


def create_index():
    # dichiarazione della variabile ix per accedere all'index
    index_manager = MangeReviewIndex()

    with open(data_path, newline='') as f:
        print("Creazione indice...")
        data = csv.DictReader(f)
        # inizializzazione del writer che permette la scrittura sull'index
        index_manager.initialize_index()

        index_manager_functions = index_manager.writer_function()

        index = 0
        for item in data:
            sys.stdout.write("\r\tDocumenti indicizzati %i" % index)
            sys.stdout.flush()
            if index == 100:
                break
            index += 1

            review = {
                **item,
                "score": float(item["score"]),
                "price_book": float(item["price_book"]),
                "negative_sentiment": float(item["negative_sentiment"]),
                "neutral_sentiment": float(item["neutral_sentiment"]),
                "positive_sentiment": float(item["positive_sentiment"]),

                "date": datetime.fromtimestamp(int(item["date"])),

            }

            # aggiunta del documento all'index
            index_manager_functions["add_document"](**review)
        index_manager_functions["save_document"]()
        print()
