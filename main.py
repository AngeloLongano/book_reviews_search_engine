import csv
import inverted_index
import os
from datetime import datetime

from sentimental_analysis import sentiment, initialize_sentiment_model

# path per il file books_ratings.csv
data_path = os.getcwd() + "/processed_data/books_rating.csv"
# ottengo le 3 variabili che servono per la sentimenti analysis [tokenizer,model,config]
model_variables = initialize_sentiment_model()

if __name__ == "__main__":
    # dichiarazione della variabile ix per accedere all'index
    ix = inverted_index.initialize_index()

    with open(data_path, newline='') as f:
        print("aperto il file")
        data = csv.DictReader(f)
        # inizializzazione del writer che permette la scrittura sull'index
        writer = ix.writer()
        # estrazione dell 3 variabili ottenute dall'inizializzazione del modello dei sentiment anlysis
        tokenizer = model_variables["tokenizer"]
        model = model_variables["model"]
        config = model_variables["config"]
        index=0
        for item in data:
            if index%100==0 :
                print("Indicizzati: ",index)
            index+=1
            # ottengo i valori della sentiment sul testo della recensione
            sentiment_analysis = sentiment(item["text"], tokenizer, model, config)

            review={
                **item,
                "score": float(item["score"]),
                "price_book":float(item["price_book"]),
                "date": datetime.fromtimestamp(int(item["date"])),
                "negative_sentiment": sentiment_analysis["negative"],
                "neutral_sentiment": sentiment_analysis["neutral"],
                "positive_sentiment" : sentiment_analysis["positive"],
            }

            # aggiunta del documento all'index
            writer.add_document(**review)
        writer.commit()

print("done")
