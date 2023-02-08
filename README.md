# BookReviewsSearchEngine

#### Installazione
Scaricare il [Data set](https://www.kaggle.com/datasets/mohamedbakhet/amazon-books-reviews).
Inserire il file Books_rating.csv nella cartella source_data.

Far partire le procedure di preprocessing con:
    
    python3 main.py
Questo comando farà partire dei moduli di python per:
- ottimizzare i dati
- fare la sentimental analysis
- creare l'indice

P.S. Nel caso in cui la cartella index sia già all'interno, vuol dire che l'indice è già creato, quindi il programma non eseguira le funzioni di preprocessing.

## Informazioni del progetto

Sentimental Analysis fatta utilizzando il [modello cardiffnlp](https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment) preso da huggingface.com.


Per eseguire una ricerca:

    python3 search_index.py

## Per eseguire i test

    python -m unittest -v .\tests\test_name.py
    
    python -m unittest -v .\tests\test_parse_data.py



#### N.B. : Assicurarsi di aver installato tutti i moduli esterni
__Utilizzare python 3.9__

_lista moduli:_

    {}