import csv

with open('books_data.csv', 'r', encoding="utf8") as file:
    reader = csv.reader(file)
    rows = []
    for row in reader:
        rows.append(row)
        print(row)
