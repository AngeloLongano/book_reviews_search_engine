from typing import Any

import numpy as np
from scipy.special import softmax
from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig

from utils.services.path_used_service import MODEL_SENTIMENT_PATH


# inizalizzazione del modello di sentiment analysis e restituzione delle variabili necessarie
def initialize_sentiment_model():
    """
    Inizializza il modello di sentiment analysis
    genera le variabili per gestire il tokenizer,configurazione e modello
    restituisce le variabili per utilizzo esterno

    """
    tokenizer = AutoTokenizer.from_pretrained(MODEL_SENTIMENT_PATH)
    config = AutoConfig.from_pretrained(MODEL_SENTIMENT_PATH)

    model = AutoModelForSequenceClassification.from_pretrained(MODEL_SENTIMENT_PATH)
    model.save_pretrained(MODEL_SENTIMENT_PATH)
    tokenizer.save_pretrained(MODEL_SENTIMENT_PATH)

    return {"tokenizer": tokenizer, "model": model, "config": config}


def sentiment(text: str, tokenizer: Any, model: Any, config: Any):
    """
    :param text: testo da analizzare
    :param tokenizer:
    :param model: 
    :param config:
    Calcola il valore di sentiment analysis di text
    restituisce tre valori di positività,neutralità e negatività
    """
    negative = 0
    neutral = 0
    positive = 0

    encoded_input = tokenizer(text, return_tensors='pt', max_length=512, truncation=True)
    output = model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    ranking = np.argsort(scores)
    ranking = ranking[::-1]

    for i in range(scores.shape[0]):

        l = config.id2label[ranking[i]]
        s = scores[ranking[i]]

        if l == "negative":
            negative = np.round(float(s), 4)
        elif l == "positive":
            positive = np.round(float(s), 4)
        else:
            neutral = np.round(float(s), 4)

    return {"negative": negative, "neutral": neutral, "positive": positive}
