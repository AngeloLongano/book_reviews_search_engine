from whoosh import scoring
from whoosh.qparser import QueryParser

from Scheme import ReviewScheme
from inverted_index import initialize_index

ix = initialize_index()

qp = QueryParser("text", schema=ReviewScheme())
q = qp.parse("I just finished the book")

with ix.searcher(weighting=scoring.TF_IDF()) as searcher:
    results = searcher.search(q)
    print("ricerca")
    print(results)
    for hit in results:
        print(hit["text"])
        print(hit.highlights("text"))