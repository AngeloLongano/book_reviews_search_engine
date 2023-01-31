from whoosh.analysis import StemmingAnalyzer
from whoosh.fields import TEXT, ID, NUMERIC, DATETIME, SchemaClass


#schema utilizzato per il documento che rappresenta ogni recensione
class Scheme(SchemaClass):
    bookId=ID(stored=True)
    userId=ID(stored=True)
    score=NUMERIC(stored=True)
    reviewDate=DATETIME(stored=True)
    reviewText=TEXT(analyzer=StemmingAnalyzer(),phrase=True)
    profileName=TEXT(stored=True)
    bookPrice=NUMERIC(stored=True)
    bookTitle=TEXT(analyzer=StemmingAnalyzer(),phrase=True)
    sentimentNeg=NUMERIC(stored=True)
    sentimentNeu=NUMERIC(stored=True)
    sentimentPos=NUMERIC(stored=True)
    summary=TEXT(stored=True)
    