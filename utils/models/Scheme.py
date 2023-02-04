from whoosh.analysis import StemmingAnalyzer
from whoosh.fields import TEXT, ID, NUMERIC, DATETIME, SchemaClass


#schema utilizzato per il documento che rappresenta ogni recensione
class ReviewScheme(SchemaClass):
    id_user=ID(stored=True)
    name_user=TEXT(stored=True)
    date=DATETIME(stored=True,sortable=True)
    title=TEXT(analyzer=StemmingAnalyzer(),phrase=True,stored=True,spelling=True)
    text=TEXT(analyzer=StemmingAnalyzer(),phrase=True,stored=True,spelling=True)
    score=NUMERIC(stored=True,sortable=True)

    id_book=ID(stored=True)
    price_book=NUMERIC(stored=True,sortable=True)
    title_book=TEXT(analyzer=StemmingAnalyzer(),phrase=True,stored=True)

    negative_sentiment=NUMERIC(stored=True,sortable=True)
    neutral_sentiment=NUMERIC(stored=True,sortable=True)
    positive_sentiment= NUMERIC(stored=True,sortable=True)
