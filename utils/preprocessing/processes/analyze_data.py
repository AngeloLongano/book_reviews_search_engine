from utils.SentimentAnalysis import SentimentAnalysis
from utils.models.DocumentModel import DocumentModel
from utils.services.optimizer_file_service import optimize_file
from utils.services.path_used_service import OPTIMIZED_DATA_PATH, ANALYZED_DATA_PATH
from utils.services.time_decorator import long_time_function

sentimentAnalyzer = SentimentAnalysis()
'''
tokenizer = model_variables["tokenizer"]
model = model_variables["model"]
config = model_variables["config"]
'''


def add_sentimental_analysis(item: DocumentModel) -> DocumentModel:
    """
    Funsione che aggiunge la sentimental analysis ad una recensione
    :param item: recensione
    :return: recensione con sentimental analysis
    """
    sentiment_analysis = sentimentAnalyzer.sentiment(item["text"])
    return {
        **item,
        "negative_sentiment": sentiment_analysis["negative"],
        "neutral_sentiment": sentiment_analysis["neutral"],
        "positive_sentiment": sentiment_analysis["positive"],
    }


@long_time_function
def analyze_data():
    """
    Funzione che crea il file con i dati con la sentiment analysis per ogni recensione
    :return:
    """
    print("Inizio sentimental analysis sui dati...")
    optimize_file(old_file_path=OPTIMIZED_DATA_PATH, new_file_path=ANALYZED_DATA_PATH,
                  parse_object=add_sentimental_analysis)
