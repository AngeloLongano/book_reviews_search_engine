from whoosh import scoring
from whoosh.qparser import QueryParser

from Scheme import ReviewScheme
from inverted_index import initialize_index
from utils.ManageReviewIndex import MangeReviewIndex



index_manager = MangeReviewIndex()

index_manager.initialize_index()

index_manager.search_index("book","text")


