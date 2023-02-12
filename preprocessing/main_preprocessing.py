from preprocessing.processes.analyze_data import analyze_data
from preprocessing.processes.create_index import create_index
from preprocessing.processes.optimize_data import optimize_data
from utils.services.path_used_service import is_there_optimized_data, is_there_analyzed_data, is_there_index_dir


def preprocessing():
    """
    Funzione principale dove vengono chiamate tutte le fasi preprocessing dei dai fino alla creazione dei vari indici per la ricerca.
    """

    if is_there_index_dir():
        print("PREPROCESSING: already DONE.")
        return

    print("PREPROCESSING:")
    if not is_there_optimized_data():
        optimize_data()
        print("OPTIMIZE DATA: done!")
        analyze_data()
        print("SENTIMENTAL ANALYSIS: done")
    else:
        print("OPTIMIZE DATA: already done!")
        if not is_there_analyzed_data():
            analyze_data()
            print("SENTIMENTAL ANALYSIS: done")
        else:
            print("SENTIMENTAL ANALYSIS: already done!")

    create_index()
    print("INDEX CREATED")
