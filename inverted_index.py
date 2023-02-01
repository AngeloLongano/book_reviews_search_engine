import whoosh.index as index

from Scheme import ReviewScheme
import os


#funzione che inizializza l'inverted index controllando la sua esistenza,se esiste si apre quello presente altrimenti si crea,si restituisce poi la variabile di accesso
def initialize_index():
    index_directory_path = os.getcwd()+"/index"
    index_directory = os.listdir(index_directory_path)
    ix = None
    if len(index_directory)==0:
        schema = ReviewScheme()
        ix = index.create_in(index_directory_path, schema)
    else:
        ix = index.open_dir(index_directory_path)
    
    return ix
