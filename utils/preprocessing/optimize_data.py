import os

from utils.OptimizeService import optimize_file
from utils.models.DocumentModel import from_dirty_to_document_model



dirty_data_path = os.getcwd() + "/source_data/books_rating.csv"
clean_data_path = os.getcwd() + '/processed_data/books_rating.csv'

def optimize_data():
    optimize_file(old_file_path=dirty_data_path,new_file_path=clean_data_path,parse_object=from_dirty_to_document_model)

