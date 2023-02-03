from utils.OptimizeService import optimize_file
from utils.sentimental_analysis import sentiment, initialize_sentiment_model

books_rating_path = "../processed_data/books_rating.csv"
books_rating_with_sentimental_path = "../processed_data/books_rating_with_sentimental.csv"

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

optimize_file(old_file_path=books_rating_path,new_file_path=books_rating_with_sentimental_path,parse_object=add_sentimental_analysis,n_documents=100)









