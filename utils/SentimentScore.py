from whoosh.scoring import BM25F


class SentimentScorer(BM25F):
    def __init__(self, fieldname, k1=1.5, b=0.75, qtf=1.0, positive_weight=1.0, negative_weight=1.0,
                 neutral_weight=1.0):
        super().__init__(fieldname, k1, b, qtf)
        self.positive_weight = positive_weight
        self.negative_weight = negative_weight
        self.neutral_weight = neutral_weight

    def scorer(self, searcher, fieldname, text, qf=1):
        field = searcher.reader().schema[fieldname]
        if field.format.is_numeric:
            return super().scorer.RawScorer(fieldname)
        else:
            return SentimentWeighting(fieldname, self, searcher, text, qf)


class SentimentWeighting(BM25F.WeightLength):
    def __init__(self, fieldname, weighting, searcher, text, qf=1):
        super().__init__(fieldname, weighting, searcher, text, qf)
        self.positive_weight = weighting.positive_weight
        self.negative_weight = weighting.negative_weight
        self.neutral_weight = weighting.neutral_weight

    def score(self, matcher):
        doc = matcher.id()
        reader = self.searcher.reader()
        positive_sentiment = reader.stored_fields(doc).get("positive_sentiment", 0.0)
        negative_sentiment = reader.stored_fields(doc).get("negative_sentiment", 0.0)
        neutral_sentiment = reader.stored_fields(doc).get("neutral_sentiment", 0.0)
        sentiment_score = (positive_sentiment * self.positive_weight) + (negative_sentiment * self.negative_weight) + (
                    neutral_sentiment * self.neutral_weight)
        return super().score(matcher) + sentiment_score

