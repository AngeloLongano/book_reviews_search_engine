from utils.services.optimizer_file_service import optimize_file
from utils.services.path_used_service import OPTIMIZED_DATA_PATH, ANALYZED_DATA_PATH
from utils.services.sentimental_analysis_service import sentiment, initialize_sentiment_model

# ottengo le 3 variabili che servono per la sentimenti analysis [tokenizer,model,config]
model_variables = initialize_sentiment_model()
tokenizer = model_variables["tokenizer"]
model = model_variables["model"]
config = model_variables["config"]


def add_sentimental_analysis(item):
    # ottengo i valori della sentiment sul testo della recensione
    sentiment_analysis = sentiment(item["text"], tokenizer, model, config)
    return {
        **item,
        "negative_sentiment": sentiment_analysis["negative"],
        "neutral_sentiment": sentiment_analysis["neutral"],
        "positive_sentiment": sentiment_analysis["positive"],
    }


def analyze_data():
    print("Inizio sentimental analysis sui dati...")
    optimize_file(old_file_path=OPTIMIZED_DATA_PATH, new_file_path=ANALYZED_DATA_PATH,
                  parse_object=add_sentimental_analysis, n_documents=10)
