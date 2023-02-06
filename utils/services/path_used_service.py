import os
from pathlib import Path

ORIGINAL_DATA_PATH = os.getcwd() + "/source_data/Books_rating.csv"
OPTIMIZED_DATA_PATH = os.getcwd() + '/processed_data/books_rating.csv'
ANALYZED_DATA_PATH = os.getcwd() + "/processed_data/books_rating_with_sentimental.csv"

INDEX_DIR_PATH = os.getcwd() + "/index"


def is_there_optimized_data() -> bool:
    return Path(OPTIMIZED_DATA_PATH).is_file()


def is_there_analyzed_data() -> bool:
    return Path(ANALYZED_DATA_PATH).is_file()


def is_there_index_dir() -> bool:
    if not os.path.isdir(INDEX_DIR_PATH):
        print("Creata cartella indice")
        os.makedirs(INDEX_DIR_PATH)
    return len(os.listdir(INDEX_DIR_PATH)) == 0
