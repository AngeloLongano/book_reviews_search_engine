from preprocessing.processes.analyze_data import analyze_data
from preprocessing.processes.create_index import create_index
from preprocessing.processes.optimize_data import optimize_data
from utils.services.path_used_service import is_there_optimized_data, is_there_analyzed_data, is_there_index_dir


def preprocessing():
    print("PREPROCESSING:")

    if not is_there_optimized_data():
        optimize_data()
    print("DATI OTTIMIZZATI")

    if not is_there_analyzed_data():
        analyze_data()

    print("SENTIMENTAL ANALYSIS FATTA")

    if is_there_index_dir():
        create_index()

    print("INDICE CREATO")


