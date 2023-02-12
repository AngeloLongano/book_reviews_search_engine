import os
from pathlib import Path

ORIGINAL_DATA_PATH = os.getcwd() + "/source_data/Books_rating.csv"
OPTIMIZED_DATA_PATH = os.getcwd() + '/processed_data/books_rating.csv'
ANALYZED_DATA_PATH = os.getcwd() + "/processed_data/books_rating_with_sentimental.csv"

INDEX_DIR_PATH = os.getcwd() + "/index"

IMAGE_PATH = os.getcwd() + "/media/book_image.jpg"


def is_there_optimized_data() -> bool:
    """ Controlla se è presente il file dei dati già ottimizzato"""
    return Path(OPTIMIZED_DATA_PATH).is_file()


def is_there_analyzed_data() -> bool:
    """ Controlla se è presente il file dei dati con la sentimental analysis"""
    return Path(ANALYZED_DATA_PATH).is_file()


def is_there_index_dir() -> bool:
    """
    Controlla se è presente l'indice,
    - se non c'è, crea la cartella e restituisce False
    - se c'è la cartella,
        - restituisce True solo se sono presenti dei file (supponendo che quei file siano di un indice già fatto),
        - restituisce False altrimenti
    """
    if not os.path.isdir(INDEX_DIR_PATH):
        print("Creata cartella indice")
        os.makedirs(INDEX_DIR_PATH)
    return len(os.listdir(INDEX_DIR_PATH)) != 0
