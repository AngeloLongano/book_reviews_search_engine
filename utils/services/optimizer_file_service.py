from __future__ import annotations

import csv
import sys
from typing import Callable

from utils.helpers.DocumentHelper import DocumentHelper
from utils.models.DocumentModel import DocumentModel


def optimize_file(old_file_path: str, new_file_path: str, parse_object: Callable[[dict], DocumentModel | None],
                  n_documents: int | None = None):
    """
    Funzione che ottimizza un file: ogni documento viene trasformato in base alla funzione parse_object

    :param old_file_path:
    :param new_file_path:
    :param parse_object: funzione che fa il parsing di ogni documento
    :param n_documents: numero documenti da analizzare
    """
    with open(old_file_path, newline='') as file_old:
        with open(new_file_path, 'w', newline='') as file_new:
            writer = csv.DictWriter(file_new, fieldnames=DocumentHelper.fields)
            writer.writeheader()
            reader = csv.DictReader(file_old)

            for index, item in enumerate(reader):
                sys.stdout.write(f"\r\tDocumenti analizzati {index}")

                if n_documents and index >= n_documents:
                    break

                parsed_item = parse_object(item)
                if parsed_item is not None:
                    writer.writerow(parsed_item)
            print("\n")
