
from ast import Dict
import numpy as np
from scipy.special import softmax
from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig

from utils.abstract.SentimentAnalysisAbstract import SentimentAnalysisAbstract
from utils.services.path_used_service import MODEL_SENTIMENT_PATH


class SentimentAnalysis(SentimentAnalysisAbstract):

    def __init__(self):

        # inizalizzazione del modello di sentiment analysis e restituzione delle variabili necessarie
        """
        Inizializza il modello di sentiment analysis
        genera le variabili per gestire il tokenizer,configurazione e modello
        restituisce le variabili per utilizzo esterno

        """
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_SENTIMENT_PATH)
        self.config = AutoConfig.from_pretrained(MODEL_SENTIMENT_PATH)

        self.model = AutoModelForSequenceClassification.from_pretrained(MODEL_SENTIMENT_PATH)
        self.model.save_pretrained(MODEL_SENTIMENT_PATH)
        self.tokenizer.save_pretrained(MODEL_SENTIMENT_PATH)

        # return {"tokenizer": tokenizer, "model": model, "config": config}

    def sentiment(self, text: str) -> Dict:
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

        # il text viene tokenizzato e trasformato in tensors con i realtivi parametri
        encoded_input = self.tokenizer(text, return_tensors='pt', max_length=512, truncation=True)
        # i tensors ottenuti vengono passati al modello
        output = self.model(**encoded_input)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)

        ranking = np.argsort(scores)
        ranking = ranking[::-1]
        #shape restituisce la struttura di scores. ES. matrice 3x3
        for i in range(scores.shape[0]):

            l = self.config.id2label[ranking[i]]
            s = scores[ranking[i]]

            if l == "negative":
                negative = np.round(float(s), 4)
            elif l == "positive":
                positive = np.round(float(s), 4)
            else:
                neutral = np.round(float(s), 4)

        return {"negative": negative, "neutral": neutral, "positive": positive}
