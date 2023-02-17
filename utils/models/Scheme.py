from whoosh.analysis import StemmingAnalyzer
from whoosh.fields import TEXT, ID, NUMERIC, DATETIME, SchemaClass


class ReviewScheme(SchemaClass):
    """
    Schema utilizzato per la creazione degli indici con whoosh
    """
    id_user = ID(stored=True)
    name_user = TEXT(stored=True)
    date = DATETIME(stored=True, sortable=True)
    title = TEXT(analyzer=StemmingAnalyzer(), phrase=True, stored=True, spelling=True)
    text = TEXT(analyzer=StemmingAnalyzer(), phrase=True, stored=True, spelling=True)
    score = NUMERIC(stored=True, sortable=True)

    id_book = ID(stored=True)
    price_book = NUMERIC(stored=True, sortable=True, decimal_places=2)
    title_book = TEXT(analyzer=StemmingAnalyzer(), phrase=True, stored=True)

    negative_sentiment = NUMERIC(stored=True, sortable=True, decimal_places=4,field_boost=2.0)
    neutral_sentiment = NUMERIC(stored=True, sortable=True, decimal_places=4,field_boost=2.0)
    positive_sentiment = NUMERIC(stored=True, sortable=True, decimal_places=4,field_boost=2.0)
