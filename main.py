import csv
import inverted_index
import os
from datetime import datetime

from sentimental_analysis import sentiment, initialize_sentiment_model

# path per il file books_ratings.csv
data_path = os.getcwd() + "/processed_data/books_rating.csv"

if __name__ == "__main__":
    # dichiarazione della variabile ix per accedere all'index
    ix = inverted_index.initialize_index()

    with open(data_path, newline='') as f:
        print("aperto il file")
        data = csv.DictReader(f)
        # inizializzazione del writer che permette la scrittura sull'index
        writer = ix.writer()

        index=0
        for item in data:
            if index%100==0 :
                print("Indicizzati: ",index)
            if index==100 :
                break
            index+=1

            review={
                **item,
                "score": float(item["score"]),
                "price_book":float(item["price_book"]),
                "negative_sentiment": float(item["negative_sentiment"]),
                "neutral_sentiment": float(item["neutral_sentiment"]),
                "positive_sentiment": float(item["positive_sentiment"]),

                "date": datetime.fromtimestamp(int(item["date"])),

            }

            # aggiunta del documento all'index
            print(review)
            writer.add_document(**review)
        writer.commit()

print("done")
