import whoosh.index as index

from Scheme import ReviewScheme
import os
from whoosh import scoring
from whoosh.qparser import QueryParser

from Scheme import ReviewScheme



class MangeReviewIndex:

    schema = ReviewScheme()
    index_path = os.getcwd() + "/index"

    def __init__(self):
        self.index_directory_path = MangeReviewIndex.index_path
        self.ix=None

    def initialize_index(self):
        index_directory = os.listdir(self.index_directory_path)
        if len(index_directory)==0:
            self.ix = index.create_in(self.index_directory_path, MangeReviewIndex.schema)
        else:
            self.ix = index.open_dir(self.index_directory_path)
    
    def search_index(self,query,field):
        query_parser = QueryParser(field, schema=MangeReviewIndex.schema)
        query_parsed = query_parser.parse(query)

        with self.ix.searcher(weighting=scoring.TF_IDF()) as searcher:
            query_results = searcher.search(query_parsed)
            print("ricerca")
            for result in query_results:
                for i in result:
                    print(i+": ",result[i])
                '''
                print(result[field],"\n")
                print(result.highlights(field))
                '''
                print("\n")
                print("\n")
    
    def writer_function(self):
        writer = self.ix.writer()
        return {"add_document":writer.add_document,"save_document":writer.commit}
            
        


