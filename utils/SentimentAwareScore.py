from whoosh.scoring import BM25F, BM25FScorer


class SentimentAwareScorer(BM25F):
    def __init__(self, k1=1.5, b=0.75, positive_boost=1, negative_boost=0, neutral_boost=0):
        super().__init__(k1, b)
        self.positive_boost = positive_boost
        self.negative_boost = negative_boost
        self.neutral_boost = neutral_boost
        print("valori ottenuti dalla classe:", self.positive_boost,self.negative_boost,self.neutral_boost)
    def scorer(self, searcher, fieldname, text, qf=1):
        field = searcher.reader().schema[fieldname]
        if not field.format.textual:
            return self.scorer.RawScorer(fieldname)
        else:
            return SentimentAwareBM25FScorer(fieldname, self, searcher, text, qf)


class SentimentAwareBM25FScorer(BM25FScorer):
    def __init__(self, fieldname, weighting: SentimentAwareScorer, searcher, text, qf=1):
        super().__init__(searcher, fieldname, text, weighting.B, weighting.K1, qf)
        self.searcher = searcher
        self.positive_boost = weighting.positive_boost
        self.negative_boost = weighting.negative_boost
        self.neutral_boost = weighting.neutral_boost
        

    def score(self, matcher):
        base_score = super().score(matcher)

        docid = matcher.id()

        doc = self.searcher.stored_fields(docid)

        positive_sentiment = float(doc.get("positive_sentiment", 0.0)) * 10
        negative_sentiment = float(doc.get("negative_sentiment", 0.0)) * 10
        neutral_sentiment = float(doc.get("neutral_sentiment", 0.0)) * 10
        #print("valori dei sentimenti: ",positive_sentiment,neutral_sentiment,negative_sentiment)
        sentiment_factor = (positive_sentiment * self.positive_boost) + (negative_sentiment * self.negative_boost) + (
                neutral_sentiment * self.neutral_boost)
        if sentiment_factor == 0:
            sentiment_factor = 1
        #print("sentiment factor:",sentiment_factor)
        return base_score * sentiment_factor
    
