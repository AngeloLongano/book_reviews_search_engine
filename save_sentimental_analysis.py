import csv

from sentimental_analysis import sentiment, initialize_sentiment_model

books_rating_path = "processed_data/books_rating.csv"
books_rating_with_sentimental_path = "processed_data/books_rating_with_sentimental.csv"

# ottengo le 3 variabili che servono per la sentimenti analysis [tokenizer,model,config]
model_variables = initialize_sentiment_model()

# estrazione dell 3 variabili ottenute dall'inizializzazione del modello dei sentiment anlysis
tokenizer = model_variables["tokenizer"]
model = model_variables["model"]
config = model_variables["config"]

def parsed_object(item):
    # ottengo i valori della sentiment sul testo della recensione
    sentiment_analysis = sentiment(item["text"], tokenizer, model, config)
    return {
               **item,
                "negative_sentiment": sentiment_analysis["negative"],
                "neutral_sentiment": sentiment_analysis["neutral"],
                "positive_sentiment": sentiment_analysis["positive"],
    }
def add_review(item,writer):
    writer.writerow(parsed_object(item))

fields=["id_user","name_user","date","title","text","score","id_book","price_book","title_book","negative_sentiment","neutral_sentiment","positive_sentiment"]
with open(books_rating_path, newline='') as file_old:
    with open(books_rating_with_sentimental_path, 'w', newline='') as file_new:
        writer = csv.DictWriter(file_new, fieldnames=fields)
        writer.writeheader()
        # lettura file csv
        reader = csv.DictReader(file_old)
        index=0
        for item in reader:
            if index%10 == 0:
                print("righe lette ",index)
            if index==100:
                break
            index+=1
            add_review(item,writer)

print("done")
print(index)
