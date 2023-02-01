import csv

csv_path = "source_data/books_rating.csv"
book_reviews = []
def is_correct(item):
    if item["Id"] != "" and item["User_id"] != "" and item["Title"] != "" and item["review/text"] != "" and item["review/score"] != "" and item["Price"] != "" :
        return True
    else:
        return False
def parsed_object(item):
    return {
                "id_user": item["User_id"],
                "name_user": item["profileName"],
                "date": item["review/time"],
                "title": item["review/summary"],
                "text": item["review/text"],
                "score": float(item["review/score"]),

                "id_book": item["Id"],
                "price_book": float(item["Price"]),
                "title_book": item["Title"],
    }
def add_review(item):
    if is_correct(item):
        book_reviews.append(parsed_object(item))


with open(csv_path, newline='') as f:
    # lettura file csv
    reader = csv.DictReader(f)
    for item in reader:
        add_review(item)


print("fine lettura")

fields=["id_user","name_user","date","title","text","score","id_book","price_book","title_book"]
with open('processed_data/books_rating.csv', 'w',newline='') as file:
    writer = csv.DictWriter(file,fieldnames=fields)
    writer.writeheader()
    writer.writerows(book_reviews)


print("done")
