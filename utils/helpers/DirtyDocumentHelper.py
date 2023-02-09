class DirtyDocumentHelper:
    fields = ["User_id",
        "profileName",
        "review/time",
        "review/summary",
        "review/text",
        "review/score",
        "Id",
        "Price",
        "Title"]

    @classmethod
    def is_valid(cls, item: dict) -> bool:
        if not item:
            return False
        else:
            for field in cls.fields:
                try:
                    if not item[field] or item[field] == "":
                        #print(field, ": value not valid")
                        return False
                except KeyError:
                    #print(field, " not present")
                    return False
            return True


