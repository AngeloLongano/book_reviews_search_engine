from __future__ import annotations

import csv
import sys
from typing import Callable

from utils.helpers.DocumentHelper import DocumentHelper
from utils.models.DocumentModel import DocumentModel

def optimize_file(old_file_path: str, new_file_path: str, parse_object: Callable[[dict], DocumentModel | None],
                  n_documents: int | None = None):
    with open(old_file_path, newline='') as file_old:
        with open(new_file_path, 'w', newline='') as file_new:
            writer = csv.DictWriter(file_new, fieldnames=DocumentHelper.fields)
            writer.writeheader()
            # lettura file csv
            reader = csv.DictReader(file_old)
            index = 0
            for item in reader:
                sys.stdout.write("\r\tDocumenti analizzati %i" % index)
                sys.stdout.flush()
                if n_documents and index == n_documents:
                    break
                index += 1
                parsed_item = parse_object(item)
                if parsed_item is not None:
                    writer.writerow(parsed_item)
            print()
