class DirtyDocumentHelper:
    """
    Classe statica per gestire i documenti con i campi non standard (documento da Kaggle)
    """

    fields = ["User_id",
              "profileName",
              "review/time",
              "review/summary",
              "review/text",
              "review/score",
              "Id",
              "Price",
              "Title"]

    @staticmethod
    def is_valid(item: dict) -> bool:
        if not item:
            return False
        else:
            for field in DirtyDocumentHelper.fields:
                try:
                    if not item[field] or item[field] == "":
                        # print(field, ": value not valid")
                        return False
                except KeyError:
                    # print(field, " not present")
                    return False
            return True
