from whoosh import scoring
from whoosh.compat import iteritems
from whoosh.scoring import WeightingModel, WeightLengthScorer, WeightScorer, BM25F


def bm25(idf, tf, fl, avgfl, B, K1):
    # idf - inverse document frequency
    # tf - term frequency in the current document
    # fl - field length in the current document
    # avgfl - average field length across documents in collection
    # B, K1 - free paramters

    return idf * ((tf * (K1 + 1)) / (tf + K1 * ((1 - B) + B * fl / avgfl)))


class CustomBM25F(BM25F):
    def final(self, searcher, docnum, score):
        print("searcher ", searcher)
        print("docnum ", docnum)
        print("score ", score)
        return score + 10

class CustomScorer(BM25F):
    def __init__(self, fieldname, boost_factor,*args, **kwargs):
        self.fieldname = fieldname
        self.boost_factor = boost_factor
        super().__init__(*args,**kwargs)

    def score(self, searcher, docnum, text, q):
        # Get the document from the searcher
        doc = searcher.stored_fields(docnum)
        # Get the value of the field to use as a boost factor
        boost_value = doc.get(self.fieldname, 1.0)
        # Calculate the original score using the BM25F algorithm
        original_score = super().score(searcher, docnum, text, q)
        # Apply the boost factor based on the value of the field
        new_score = original_score * (1.0 + self.boost_factor * boost_value)
        return new_score


class CustomWeighting(WeightingModel):
    """Implements the custom BM25F scoring algorithm.
    """

    def __init__(self, B=0.75, K1=1.2, **kwargs):
        """

        >>> from whoosh import scoring
        >>> # Set a custom B value for the "content" field
        >>> w = scoring.BM25F(B=0.75, content_B=1.0, K1=1.5)

        :param B: free parameter, see the BM25 literature. Keyword arguments of
            the form ``fieldname_B`` (for example, ``body_B``) set field-
            specific values for B.
        :param K1: free parameter, see the BM25 literature.
        """

        self.B = B
        self.K1 = K1

        self._field_B = {}
        for k, v in iteritems(kwargs):
            if k.endswith("_B"):
                fieldname = k[:-2]
                self._field_B[fieldname] = v

    def supports_block_quality(self):
        return True

    def scorer(self, searcher, fieldname, text, qf=1):
        if not searcher.schema[fieldname].scorable:
            return WeightScorer.for_(searcher, fieldname, text)

        if fieldname in self._field_B:
            B = self._field_B[fieldname]
        else:
            B = self.B
        print("self ")
        return CustomScorer(searcher, fieldname, text, B, self.K1, qf=qf)


class CustomScorer(WeightLengthScorer):
    def __init__(self, searcher, fieldname, text, B, K1, qf=1):
        # IDF and average field length are global statistics, so get them from
        # the top-level searcher
        # text --> query
        parent = searcher.get_parent()  # Returns self if no parent
        self.idf = parent.idf(fieldname, text)
        w = scoring.BM25F(B=0.75, content_B=1.0, K1=1.5)

        positive_query = text
        print("positive query ", positive_query)
        # f"{text} AND positive_sentiment: [0.5 TO 1]"
        self.positive_matcher = parent.postings(fieldname, text, weighting=w, qf=1)
        # text: "awesome book"
        # AND
        # positive_sentiment: [0.5 TO 1]
        self.searcher = searcher
        self.fieldname = fieldname
        self.text = text

        self.avgfl = parent.avg_field_length(fieldname) or 1

        self.B = B
        self.K1 = K1
        self.qf = qf
        self.setup(searcher, fieldname, text)

    def _score(self, weight, length):
        standard = bm25(self.idf, weight, length, self.avgfl, self.B, self.K1)
        bm25F = scoring.BM25F().scorer(self.searcher, self.fieldname, self.text).score(self.positive_matcher)
        return standard * 0.4 + bm25F * 0.6
