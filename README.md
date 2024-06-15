# Book Reviews Search Engine

#### N.B. : Make sure you have installed all external modules
__Use python 3.10__

_list of modules:_
 requirements.txt

#### To install external modules, run the following command:

    pip install -r requirements.txt



## Project Execution

To start the project, run the command:

    
    python3 main.py

NB!!
To run the project, you need to have the index folder containing the files generated by the whoosh index.

The index folder __is already provided__ in the project zip version.


## Installation
__The installation phase is ONLY necessary if the index folder is not present__

Download the [Data set](https://www.kaggle.com/datasets/mohamedbakhet/amazon-books-reviews).
Insert the Books_rating.csv file into the source_data folder.

Run the preprocessing procedures with:
    
    python3 main.py

This command will start python modules to:
- Optimize data
- Perform sentiment analysis
- Create the index

P.S. If the index folder is already present, it means that the index has already been created, so the program will not execute the preprocessing functions.

To re-index the data, simply delete the index folder and restart the project..

# Query Execution

To execute searches, you have a search bar and some advanced search options in the sidebar.

The fields on which searches can be performed are:
- __text__ "the review field"
- __title__ "the title of the review"
- __title_book__ "the title of the book"
- __price_book__ "the price of the book"
- __date__ "the date of writing the review"
- __score__ "the score assigned by the user"
- __negative_sentiment__ "negative sentiment value"
- __positive_sentiment__ "positive sentiment value"
- __neutral_sentiment__ "neutral sentiment value"

To search a specific field, simply type the following command::

    campo:term
    campo:"phrase to search"

If you want to search for a phrase, you must use quotes.

    text:"a very long phrase"

If the field is not specified, the search is done by default on the text field.

Binary operators can be used within the search, also using parentheses to specify the execution order.

    text:"i like this book" AND (title_book:great OR title_book:amazing)

In addition to text search, the options in the sidebar can be used in the __sentiment__ field to choose the desired sentiment type:
- None
- Positive
- Negative
- Neutral 

You can also sort the results according to the value of the following fields by selecting it from __sort by__:
- None
- Price
- Negative
- Positive
- Neutral
- Score
- Date

You can also specify the maximum number of results you want to display by specifying it in the __max number of results__ field.

You can also change the order from ascending to descending and vice versa of the results obtained from the filters used, using the __reverse sort__ button.

For every search made on the text field, the results returned in the graphical interface will show __only__ the part of the text where a query match was found, to see the complete text of the result just click on __full review__ and view it.

For all other searches made on fields other than text, the text field can be viewed in the full review.

# Benchmark
To view the __UINs__ and their respective translations into the query language, refer to the __queries.txt__ file in the __static_data__ folder.

__NB!__

The at symbol @ in queries indicates that you need to select the sentiment type from the menu in the sidebar in the __sentiment__ dropdown.


The DCG.py file computes the benchmark calculations,based on the file becnhmark_query.json in the static_data folder, in which you can find the different scores given to each retrievd document for each query.

    python3 DCG.py
To check the results graph,please refer to the following google sheet [google sheet document](https://docs.google.com/spreadsheets/d/1g4fKIfJyTewnV1KJ8T1tmrHmAXVme5cmCmx9ADoGdCw/edit?usp=sharing)

## Project informations

Sentimental Analysis made using the model [model cardiffnlp](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest) taken from huggingface.com.

Tht sentiment analysis model generates the __cardiffnlp__ folder in which it saves all the information it needs to run,this folder will be created automatically the first time you run the program.

The Gui was made using the library [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)

During the execution of the program especially in the search part,you might encounter the __Not responding__ error, this is normal, just give it a couple of seconds and everything will be alright.


_If the results box is too small for your screen, change the values in the file __App.py__ in the folder __gui__:_

    RESULT_CANVAS_HEIGHT = 450
    RESULT_CANVAS_WIDTH = 800

    # normal 450 x 800
    # matebook d15 900 x 1500







