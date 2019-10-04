import unittest

from main import validate_file


class TestCase(unittest.TestCase):

    def test_validate_input(self):
        file_path = validate_file('not_exist.file')
        self.assertEqual(file_path, None)

        file_path = validate_file(__file__)
        self.assertTrue(file_path)
