# This is a sample Python script.
from utils.parse_data import DataParsed
from utils.preprocessing.sentiment_analysis import sentiment_analysis


# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(DataParsed)
    a = DataParsed("ciao")
    print(a)
    print(sentiment_analysis("Wow, NLTK is really powerful!"))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
