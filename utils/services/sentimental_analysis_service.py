import numpy as np
from scipy.special import softmax
from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
MODEL = f"cardiffnlp/twitter-roberta-base-sentiment-latest"

#inizalizzazione del modello di sentiment analysis e restituzione delle variabili necessarie
def initialize_sentiment_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    config = AutoConfig.from_pretrained(MODEL)

    model = AutoModelForSequenceClassification.from_pretrained(MODEL)
    model.save_pretrained(MODEL)
    tokenizer.save_pretrained(MODEL)

    return {"tokenizer":tokenizer,"model":model,"config":config}


#calcolo della sentiment sulla entry restituendo 3 valori di positivià,negatività e neutralità
def sentiment(text,tokenizer,model,config):
    
    negative = 0
    neutral = 0
    positive = 0

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
            negative = np.round(float(s), 4)
        elif l == "positive":
            positive = np.round(float(s), 4)
        else:
            neutral = np.round(float(s), 4)

    return {"negative":negative,"neutral":neutral,"positive":positive}