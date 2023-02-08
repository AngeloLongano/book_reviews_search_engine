import unittest

from utils.helpers.DirtyDocumentHelper import DirtyDocumentHelper

CORRECT_OBJECT = {
    "User_id": 122,
    "profileName": "profileName",
    "review/time": "12211111",
    "review/summary": "title",
    "review/text": "text",
    "review/score": 12,

    "Id": "11",
    "Price": 12.20,
    "Title": "text",
}


class TestValidationDirtyDocument(unittest.TestCase):
    def test_correct_object(self):
        self.assertTrue(DirtyDocumentHelper.is_valid(CORRECT_OBJECT))

    def test_empty_object(self):
        test_object = {}
        self.assertFalse(DirtyDocumentHelper.is_valid(test_object))

    def test_not_complete_object(self):
        test_object = {"User_id": 123}
        self.assertFalse(DirtyDocumentHelper.is_valid(test_object))

    def test_wrong_field_object(self):
        test_object = {"id_bok": "ciao"}
        self.assertFalse(DirtyDocumentHelper.is_valid(test_object))

    def test_none_field_object(self):
        test_object = {**CORRECT_OBJECT, "User_id": None}
        self.assertFalse(DirtyDocumentHelper.is_valid(test_object))
