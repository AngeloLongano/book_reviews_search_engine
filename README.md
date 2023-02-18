# BookReviewsSearchEngine

#### N.B. : Assicurarsi di aver installato tutti i moduli esterni
__Utilizzare python 3.10__

_lista moduli:_
 requirements.txt

#### Per installare i moduli esterni, eseguire il seguente comando:

    pip install -r requirements.txt



## Esecuzione progetto

Per avviare il progetto basta eseguire il comando 
    
    python3 main.py

NB!!
Per far partire il progetto basta avere la cartella index con all'interno i file generati dall'index di whoosh.

La cartella index __è già fornita__ nella versione zip del progetto.


## Installazione
__La fase di installazione serve SOLO se la cartella index non è presente__

Scaricare il [Data set](https://www.kaggle.com/datasets/mohamedbakhet/amazon-books-reviews).
Inserire il file Books_rating.csv nella cartella source_data.

Far partire le procedure di preprocessing con:
    
    python3 main.py

Questo comando farà partire dei moduli di python per:
- ottimizzare i dati
- fare la sentimental analysis
- creare l'indice

P.S. Nel caso in cui la cartella index sia già all'interno, vuol dire che l'indice è già creato, quindi il programma non eseguira le funzioni di preprocessing.

Per reindicizzare i dati basta eliminare la cartella index e far ripartire il progetto.

# Esecuzione query

Per eseguire le ricerche si hanno a dispozione una barra di ricerca e alcune opzioni di ricerca avanzata nella barra laterale.

I campi sui qualli si possono eseguire le ricerche sono:
- __text__ "il campo della recensione"
- __title__ "il titolo della recensione"
- __title_book__ "il titolo del libro"
- __price_book__ "il prezzo del libro"
- __date__ "la data della scrittura della recensione"
- __score__ "il voto assegnato dall'utente"
- __negative_sentiment__ "valore di sentiment negativo"
- __positive_sentiment__ "valore di sentiment positivo"
- __neutral_sentiment__ "valore di sentiment neutrale"

Per fare la ricerca su un campo specifico basta scrivere il seguente comando:

    campo:termine
    campo:"frase da cercare"

Se si vuole fare ricerca di una frase e necessario utilizzare gli apici.

    text:"a very long phrase"

Se non si specifica il campo, la ricerca di default viene fatta sul campo text.

Si possono utilizzare gli operatori binari all'interno della ricerca, utilizzando anche le parentesi chiuse per specificare l'ordine di esecuzione.

    text:"i like this book" AND (title_book:great OR title_book:amazing)

Oltre alla ricerca testuale si possono utlizzare le opzioni della barra laterale nel campo __sentiment__ per scegliere la tipologia di sentimento voluta:
- None
- Positive
- Negative
- Neutral 

Si può anche fare l'ordinamento dei risultati secondo il valore dei seguenti campi selzionandolo da __sort by__:
- None
- Price
- Negative
- Positive
- Neutral
- Score
- Date

Si può anche specificare il numero di risultati massimi che si vuole visualizzare specificandolo nel campo __max number of results__

# Benchmark
Per visualizzare le __UIN__ e le loro relative traduzioni in query nel linguaggio di interrogazione,fare riferimento al file __queries.txt__ nella cartella __static_data__

__NB!__

La chiocciola __@__ nelle query indica che bisogna selezionare la tipologia di sentiment dal menu nella barra laterale nel campo __sentiment__

il file DCG.py esegue i calcoli di benchmark,basandosi sul file benchmark_query.json nella cartella static_data,nel quale si trovano i vari score assegnati ad ogni documento restituito per ogni query

    python3 DCG.py
Per vedere anche eventuali grafici dei risultati si prega di visualizzare [il foglio di calcolo relativo](https://docs.google.com/spreadsheets/d/1g4fKIfJyTewnV1KJ8T1tmrHmAXVme5cmCmx9ADoGdCw/edit?usp=sharing)

## Informazioni del progetto

Sentimental Analysis fatta utilizzando il [modello cardiffnlp](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest) preso da huggingface.com.

Il modello di sentiment genera la cartella __cardiffnlp__ nel quale salva le informazioni del modello,nel caso non sia presente,questa verrà create in automatico alla prima esecuzione del programma.

L'interfaccia grafica è stata sviluppata utilizazndo la libreria [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)

Durante l'esecuzione è normale che il prgramma dia il messaggio __"Non risponde"__ mentra fa la ricerca, attendere un paio di secondi e i risultati appariranno.

_Se il box nel quale vengono visualizzati i risultati di ricerca dovesse essere troppo piccolo, cambiare i valori delle costanti nel file __App.py__ nella cartella __gui__:_

    RESULT_CANVAS_HEIGHT = 450
    RESULT_CANVAS_WIDTH = 800

    # normal 450 x 800
    # matebook d15 900 x 1500







