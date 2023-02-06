import os
from pathlib import Path

from utils.preprocessing.create_index import create_index
from utils.preprocessing.optimize_data import optimize_data
from utils.preprocessing.save_sentimental_analysis import save_sentimental_analysis

clean_data_path = Path(os.getcwd() + '/processed_data/books_rating.csv')
books_rating_with_sentimental_path = Path(os.getcwd() + "/processed_data/books_rating_with_sentimental.csv")
index_path = os.getcwd() + "/index"
def preprocessing():
    if not clean_data_path.is_file():
        optimize_data()
    if not books_rating_with_sentimental_path.is_file():
        save_sentimental_analysis()
    if len(os.listdir(index_path))==0:
        create_index()
