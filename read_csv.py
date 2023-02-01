import csv
import inverted_index
import os
from datetime import datetime

from sentimental_analysis import sentiment,initialize_sentiment_model

#path per il file books_ratings.csv
csv_path = os.getcwd()+"/source_data/books_rating.csv"
#ottengo le 3 variabili che servono per la sentimenti analysis [tokenizer,model,config]
model_variables=initialize_sentiment_model()
#numero di record che vogliamo
number_of_records = 10

if __name__ == "__main__":

    #dichiarazione della variabile ix per accedere all'index
    ix = inverted_index.initialize_index()
    
    with open(csv_path,newline='') as f:
        #lettura file csv
        reader = csv.DictReader(f)
        #variabile per il conteggio di record presi
        index = 0
        #inizializzazione del writer che permette la scrittura sull'index
        writer = ix.writer()
        #estrazione dell 3 variabili ottenute dall'inizializzazione del modello dei sentiment anlysis
        tokenizer = model_variables["tokenizer"]
        model = model_variables["model"]
        config = model_variables["config"]

        for item in reader:
            #numero di record che vogliamo
            if index == number_of_records:
                break
            else:
                if item["Id"] != "" and item["User_id"] != "" and item["Title"] != "" and item["review/text"] != "" and item["review/score"] != "" and item["Price"] != "":
                    
                    #ottengo i valori della sentiment sul testo della recensione 
                    results = sentiment(item["review/text"],tokenizer,model,config)
                    #oggetto con i campi del documento da inserire nell'index
                    review = {
                        "bookId":item["Id"],
                        "userId":item["User_id"],
                        "score":float(item["review/score"]),
                        "reviewDate":datetime.fromtimestamp(int(item["review/time"])),
                        "reviewText":item["review/text"],
                        "profileName":item["profileName"],
                        "bookPrice":float(item["Price"]),
                        "bookTitle":item["Title"],
                        "sentimentNeg":results["sentimentNeg"],
                        "sentimentNeu":results["sentimentNeu"],
                        "sentimentPos":results["sentimentPos"],
                        "summary":item["review/summary"]
                        }
                    #aggiunta del deocumento all'index
                    inverted_index.add_document_to_index(writer,review)
                    #stampa per debugging
                    print(review)
                    print("\n")
                    print("\n")
                    #aumento di 1 solo se la entry è effettivamente stata inserita,in questo modo prendo effettivamente n record validi e non solo i primi n record disponibili
                    index += 1
        #chiusura del writer dopo l'inserimento di tutti i documenti
        writer.commit()
                    