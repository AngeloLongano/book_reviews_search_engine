import whoosh.index as index

import Scheme
import os


#funzione che inizializza l'inverted index controllando la sua esistenza,se esiste si apre quello presente altrimenti si crea,si restituisce poi la variabile di accesso
def initialize_index():
    index_directory_path = os.getcwd()+"/index"
    index_directory = os.listdir(index_directory_path)
    ix = None
    if len(index_directory)==0:
        schema = Scheme.Scheme()
        ix = index.create_in(index_directory_path, schema)
    else:
        ix = index.open_dir(index_directory_path)
    
    return ix
#aggiunta del documento all'index
def add_document_to_index(writer,review):
    
    writer.add_document(
        bookId=review["bookId"], 
        userId=review["userId"],
        score=review["score"],
        reviewDate=review["reviewDate"],
        reviewText=review["reviewText"],
        profileName=review["profileName"],
        bookPrice=review["bookPrice"],
        bookTitle=review["bookTitle"],
        sentimentNeg=review["sentimentNeg"],
        sentimentNeu=review["sentimentNeu"],
        sentimentPos=review["sentimentPos"],
        summary=review["summary"],
        )
    
