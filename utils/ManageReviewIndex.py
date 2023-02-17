import os
from ast import Dict

import whoosh.index as index
from whoosh import scoring
from whoosh.qparser import QueryParser

from utils.SentimentAwareScore import SentimentAwareScorer
from utils.abstract.ManageIndexAbstract import ManageIndexAbstract
from utils.models.Scheme import ReviewScheme
from utils.services.path_used_service import INDEX_DIR_PATH


class MangeReviewIndex(ManageIndexAbstract):
    """
    Classe che gestisce tutte le funzionalità dell'index
    """
    schema = ReviewScheme()

    def __init__(self):
        """
        Costruttore della classe
        inizializza le variabili di istanza
        """
        self.index_directory_path = INDEX_DIR_PATH
        self.ix = None
        self.default_field = "text"

        index_directory = os.listdir(self.index_directory_path)
        if len(index_directory) == 0:
            self.ix = index.create_in(self.index_directory_path, MangeReviewIndex.schema)
        else:
            self.ix = index.open_dir(self.index_directory_path)

    def search_index(self, query: str, field: str, sentiment: str, max_results: int, reversed_sort: int, sort_by: str,
                     ):
        """
        La funzione si occupa di fare una ricerca all'interno del nostro index utilizzando i parametri forniti

        :param query:
        :param field:
        :param sentiment:
        :param max_results:
        :param reversed_sort:
        :param sort_by:
        :return:
        """
        
        sort_params = {}
        # Questo serve in modo da avere anche i risultati senza scegliere un sort specifico
        if (sort_by != "None"):
            sort_params["sortedby"] = sort_by

        query_parser = QueryParser(self.default_field, schema=MangeReviewIndex.schema)
        query_parsed = query_parser.parse(query)
        print("query ",query)
        print("query parsed ",query_parsed)
        results = []
        #inizializzazione dei boost dei vari sentimenti
        positive_boost = 0
        negative_boost = 0
        neutral_boost = 0
        k1 = 0.75
        b = 0.75
        print("Sentiment choosen:",sentiment)
        if sentiment == "positive_sentiment":
            positive_boost = 2
        elif sentiment == "neutral_sentiment":
            neutral_boost = 2
        elif sentiment == "negative_sentiment":
            negative_boost = 2
        
        with self.ix.searcher(weighting=SentimentAwareScorer(k1,b,positive_boost, negative_boost, neutral_boost)) as searcher:

            query_results = searcher.search(query_parsed, **sort_params, reverse=reversed_sort,
                                            limit=max_results)

            query_results_scored = query_results.scored_length()
            print("ricerca...")
            print("----------RESULTS-----------")
            print("Scored results: ", query_results_scored)
            print("Total estimated results between: ", query_results.estimated_min_length(), "and",
                  query_results.estimated_length())

            for result in query_results:
                if len(results) >= max_results:
                    break
                document = {}
                for i in result:
                    document[i] = result[i]

                    if i == "text":
                        print(i + ": ", result[i][:300] + "...")
                    else:
                        print(i + ": ", result[i])
                document["highlights"] = result.highlights(field)
                document["ranking_score"] = result.score
                results.append(document)
                
                print("score",result.score)
                print("boost",result.__dict__)
                print(result[field], "\n")
                print(result.highlights(field))

                print("\n")
                print("\n")

        return results

    def writer_function(self) -> Dict:
        """
        Restituisce le due funzioni per aggiungere un documento e per chiudere l'index scrivendo le modifiche
        :return: {"add_document", "save_document"}
        """
        writer = self.ix.writer()
        return {"add_document": writer.add_document, "save_document": writer.commit}

    def suggest_words(self, mistyped_word: str):
        """
        Restituisce delle possibili correzioni al termine in mistyped_word usando il corpus dell'index
        :param mistyped_word:
        """
        with self.ix.searcher() as s:
            corrector = s.corrector("text")
            print(corrector.suggest(mistyped_word, limit=3))

    def correct_query(self, query):
        """
        Restituisce una correzione della query presente in query

        :param query:
        :return:
        """
        query_parser = QueryParser(self.default_field, schema=MangeReviewIndex.schema)
        query_parsed = query_parser.parse(query)

        with self.ix.searcher() as s:
            corrected = s.correct_query(query_parsed, query)
            if corrected.query != query_parsed:
                print("Did you mean:", corrected.string + "?")
                return corrected.string
