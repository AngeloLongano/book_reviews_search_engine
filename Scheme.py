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

class ReviewScheme(SchemaClass):
    id_user=ID(stored=True)
    name_user=TEXT(stored=True)
    date=DATETIME(stored=True)
    title=TEXT(analyzer=StemmingAnalyzer(),phrase=True)
    text=TEXT(analyzer=StemmingAnalyzer(),phrase=True)
    score=NUMERIC(stored=True)

    id_book=ID(stored=True)
    price_book=NUMERIC(stored=True)
    title_book=TEXT(analyzer=StemmingAnalyzer(),phrase=True)

    negative_sentiment=NUMERIC(stored=True)
    neutral_sentiment=NUMERIC(stored=True)
    positive_sentiment= NUMERIC(stored=True)
