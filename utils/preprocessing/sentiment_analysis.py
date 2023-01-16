
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


def init_nltk():
    nltk.download('vader_lexicon')


def sentiment_analysis(message: str):
    ## sentiment da fare insieme al raiting
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(message)



