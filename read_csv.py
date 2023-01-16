import csv
import json

from utils.parse_data import DataParsed

class Prova:
    def __int__(self,a):
        self.a=a



if __name__ == '__main__':
    ciao = Prova("a") ## non va
    with open('source_data/books_data.csv', 'r', encoding="utf8") as file:
        reader = csv.reader(file)
        with open('sample.json', 'w') as json_file:
            for row in reader:
                print(row)
                #data = DataParsed(row)
                # json.dump(data.get_data(), json_file)
