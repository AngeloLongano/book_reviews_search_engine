from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
import numpy as np
from scipy.special import softmax
import csv,uuid

if __name__ == "__main__":

    MODEL = f"cardiffnlp/twitter-xlm-roberta-base-sentiment"

    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    config = AutoConfig.from_pretrained(MODEL)

    model = AutoModelForSequenceClassification.from_pretrained(MODEL)
    model.save_pretrained(MODEL)
    tokenizer.save_pretrained(MODEL)


    with open('books_rating.csv',newline='') as f:
        reader = csv.DictReader(f)
        reviews = {}
        users = {}
        books = {}
        index = 1
        for item in reader:
            if index == 50:
                break
            else:
                if item["Id"] != "" and item["User_id"] != "" and item["Title"] != "" and item["review/text"] != "" and item["review/score"] != "" and item["Price"] != "":
                    review = {
                        "bookId":item["Id"],
                        "userId":item["User_id"],
                        "score":item["review/score"],
                        "helpfulness":item["review/helpfulness"],
                        "reviewDate":item["review/time"],
                        "review":item["review/text"],
                        "summary":item["review/summary"]
                        }
                    user = {"userId":item["User_id"],"profileName":item["profileName"]}
                    books[item["Id"]] = {"title":item["Title"],"price":item["Price"]}
                    reviews[uuid.uuid4()]=review
                    users[item["User_id"]]=user
            index += 1

    for r in reviews:
        
        #text = "I bought this book because I read some glowing praise on an online library site. Unfortunately, I was deeply disappointed by page three. I always buy books in the hope and expectation of having an enjoyable read, not to criticise. However, this book is in urgent need of good editing -- though quite possibly editing alone wouldn't save it. Examples: a bed squeaks slightly and sharply in the same sentence; a nightgown hangs freely over her girlish figure and olive colored complexion; coffee aromas huddle; rumbling clouds huddle (as well as the coffee?); she prepared to sip her coffee beneath the wrath of God... cuddled within the arms of a strong breeze; (the wrath of God is a breeze?); the Columbian (stet) coffee aroma danced beneath her sculpted tan nose; the coffee bean fragrance tangoed within her body; she placed her thick pink lips against the warm cup;... and so on, all by page three. It is quite possible that the storyline is deeply moving. I'll never know because I can't bring myself to continue. Sorry."
        encoded_input = tokenizer(reviews[r]["review"], return_tensors='pt',max_length=512,truncation=True)
        output = model(**encoded_input)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)

        ranking = np.argsort(scores)
        ranking = ranking[::-1]
        print(r,reviews[r])
        for i in range(scores.shape[0]):
            l = config.id2label[ranking[i]]
            s = scores[ranking[i]]
            print(f"{i+1}) {l} {np.round(float(s), 4)}")
        print("----------------------------\n")