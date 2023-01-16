from utils.models.structure_models import DocumentModel


class DataParsed:
    id = 0

    def __int__(self, row):
        self.row = row
        id += 1

    def get_data(self) -> DocumentModel:
        return {'id_document': id, 'title': self.row[0]}


