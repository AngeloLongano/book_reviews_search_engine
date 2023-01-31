import csv
import json

from utils.parse_data import DataParsed


book_reviews = []
with open('source_data/books_rating.csv', 'r', encoding="utf8") as file:
    reader = csv.reader(file)
    for row in reader:
            book_reviews.append({
                "id_book": row[0],
                "title_book": row[1],
                "utility": row[5],
                "title": row[8],
                "text" : row[9],
                "score": row[6],
            })

print("fine lettura")
with open('sample.json', 'w') as json_file:
    json.dump(book_reviews, json_file)

print("done")
