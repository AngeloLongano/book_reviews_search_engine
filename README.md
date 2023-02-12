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

Sentimental Analysis fatta utilizzando il [modello cardiffnlp](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest) preso da huggingface.com.


Per eseguire una ricerca:

    python3 search_index.py

## Per eseguire i test

    python -m unittest -v .\tests\test_name.py
    
    python -m unittest -v .\tests\test_parse_data.py



#### N.B. : Assicurarsi di aver installato tutti i moduli esterni
__Utilizzare python 3.9__

_lista moduli:_
 https://github.com/AngeloLonganoUni/BookReviewsSearchEngine/blob/master/requirements.txt

# Per installare i moduli esterni, eseguire il seguente comando:

    pip install -r requirements.txt


# Struttura progetto

    BookReviewsSearchEngine
    |
    ├── gui
    │   ├── __init__.py
    │   ├── App.py
    │   └── top_level_window.py
    │   
    ├── preprocessing
    |   |
    |   ├── __init__.py
    |   ├── main_preprocessing.py
    |   └── processes
    |       |
    |       ├── __init__.py
    |       ├── analyze_data.py
    |       ├── create_index.py
    |       └── optimize_data.py
    |
    ├── test
    |   |
    |   ├── __init__.py
    |   └── test_parse_data.py
    |
    ├── utils
    |    |
    |    ├── ManageReviewIndex.py
    |    ├── helpers
    |    |   |
    |    |   ├── __init__.py
    |    |   ├── DirtyDocumentHelper.py
    |    |   └── DocumentHelper.py
    |    |
    |    ├── models
    |    |   |
    |    |   ├── __init__.py
    |    |   ├── DocumentModel.py
    |    |   └── Scheme.py
    |    |
    |    └── services
    |        |
    |        ├── __init__.py
    |        ├── optimizer_file_service.py
    |        ├── path_used_service.py
    |        ├── sentimental_analysis_service.py
    |        └── time_decorator.py
    |
    └── main.py


