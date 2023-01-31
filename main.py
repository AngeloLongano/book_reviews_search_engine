import json

with open("sample.json","r") as f:
    book_reviews = json.load(f)

print(book_reviews)
