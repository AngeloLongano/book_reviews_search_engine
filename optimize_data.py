import csv

from sentimental_analysis import sentiment, initialize_sentiment_model

csv_path = "source_data/books_rating.csv"
book_reviews = []
# ottengo le 3 variabili che servono per la sentimenti analysis [tokenizer,model,config]
model_variables = initialize_sentiment_model()

# estrazione dell 3 variabili ottenute dall'inizializzazione del modello dei sentiment anlysis
tokenizer = model_variables["tokenizer"]
model = model_variables["model"]
config = model_variables["config"]
def is_correct(item):
    if item["Id"] != "" and item["User_id"] != "" and item["Title"] != "" and item["review/text"] != "" and item["review/score"] != "" and item["Price"] != "" :
        return True
    else:
        return False
def parsed_object(item):
    # ottengo i valori della sentiment sul testo della recensione
    sentiment_analysis = sentiment(item["review/text"], tokenizer, model, config)
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
                "negative_sentiment": sentiment_analysis["negative"],
                "neutral_sentiment": sentiment_analysis["neutral"],
                "positive_sentiment": sentiment_analysis["positive"],
    }
def add_review(item,writer):
    if is_correct(item):
        writer.writerow(parsed_object(item))

fields=["id_user","name_user","date","title","text","score","id_book","price_book","title_book","negative_sentiment","neutral_sentiment","positive_sentiment"]
with open(csv_path, newline='') as file_old:
    with open('processed_data/books_rating.csv', 'w', newline='') as file_new:
        writer = csv.DictWriter(file_new, fieldnames=fields)
        writer.writeheader()
        # lettura file csv
        reader = csv.DictReader(file_old)
        index=0
        for item in reader:
            if index%100 == 0:
                print("righe lette ",index)
            if index>5000:
                break
            index+=1
            add_review(item,writer)


print("done")
