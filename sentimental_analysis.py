import numpy as np
from scipy.special import softmax
from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig


#inizalizzazione del modello di sentiment analysis e restituzione delle variabili necessarie
def initialize_sentiment_model():

    model = f"cardiffnlp/twitter-xlm-roberta-base-sentiment"

    tokenizer = AutoTokenizer.from_pretrained(model)
    config = AutoConfig.from_pretrained(model)

    model = AutoModelForSequenceClassification.from_pretrained(model)
    model.save_pretrained(model)
    tokenizer.save_pretrained(model)

    return {"tokenizer":tokenizer,"model":model,"config":config}


#calcolo della sentiment sulla entry restituendo 3 valori di positivià,negatività e neutralità
def sentiment(text,tokenizer,model,config):
    
    sentiment_neg = 0
    sentiment_neu = 0
    sentiment_pos = 0

    encoded_input = tokenizer(text, return_tensors='pt',max_length=512,truncation=True)
    output = model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    ranking = np.argsort(scores)
    ranking = ranking[::-1]

    for i in range(scores.shape[0]):
        l = config.id2label[ranking[i]]
        s = scores[ranking[i]]
        #in base alla label assegno il valore alla variabile specifica
        if l == "negative":
            sentiment_neg = np.round(float(s), 4)
        elif l == "positive":
            sentiment_pos = np.round(float(s), 4)
        else:
            sentiment_neu = np.round(float(s), 4)

    return {"sentiment_neg":sentiment_neg,"sentiment_neu":sentiment_neu,"sentiment_pos":sentiment_pos}