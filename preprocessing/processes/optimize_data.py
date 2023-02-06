from utils.models.DocumentModel import from_dirty_to_document_model
from utils.services.optimizer_file_service import optimize_file
from utils.services.path_used_service import ORIGINAL_DATA_PATH, OPTIMIZED_DATA_PATH


def optimize_data():
    print("Inizio ottimizzazione dati...")
    optimize_file(old_file_path=ORIGINAL_DATA_PATH, new_file_path=OPTIMIZED_DATA_PATH,
                  parse_object=from_dirty_to_document_model)
