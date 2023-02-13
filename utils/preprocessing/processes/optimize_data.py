from __future__ import annotations

from utils.helpers.DirtyDocumentHelper import DirtyDocumentHelper
from utils.helpers.DocumentHelper import DocumentHelper
from utils.models.DocumentModel import DocumentModel
from utils.services.optimizer_file_service import optimize_file
from utils.services.path_used_service import ORIGINAL_DATA_PATH, OPTIMIZED_DATA_PATH
from utils.services.time_decorator import time_function


def from_dirty_to_document_model(dirty_item: dict) -> DocumentModel | None:
    """
    Funzione che verifica la validità del documento e nel caso lo serializza in base al modello DocumentModel
    :param dirty_item: documento dal file esterno
    :return: documento con i parametri standard, altrimenti None
    """
    if DirtyDocumentHelper.is_valid(dirty_item):
        return DocumentHelper.from_dirty(dirty_item)
    return

@time_function
def optimize_data():
    """
    Funzione che crea un file con i dati puliti (senza documenti non validi)
    :return:
    """
    print("Inizio ottimizzazione dati...")
    optimize_file(old_file_path=ORIGINAL_DATA_PATH, new_file_path=OPTIMIZED_DATA_PATH,
                  parse_object=from_dirty_to_document_model)
