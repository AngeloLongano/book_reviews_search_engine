from __future__ import annotations

from utils.helpers.DirtyDocumentHelper import DirtyDocumentHelper
from utils.helpers.DocumentHelper import DocumentHelper
from utils.models.DocumentModel import DocumentModel
from utils.services.optimizer_file_service import optimize_file
from utils.services.path_used_service import ORIGINAL_DATA_PATH, OPTIMIZED_DATA_PATH


def from_dirty_to_document_model(dirty_item: dict) -> DocumentModel | None:
    if DirtyDocumentHelper.is_valid(dirty_item):
        return DocumentHelper.from_dirty(dirty_item)
    return


def optimize_data():
    print("Inizio ottimizzazione dati...")
    optimize_file(old_file_path=ORIGINAL_DATA_PATH, new_file_path=OPTIMIZED_DATA_PATH,
                  parse_object=from_dirty_to_document_model)
