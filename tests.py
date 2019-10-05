import unittest

from main import validate_file, read_line, word_count


class TestCase(unittest.TestCase):

    def test_validate_input(self):
        file_path = validate_file('not_exist.file')
        self.assertEqual(file_path, None)

        file_path = validate_file(__file__)
        self.assertTrue(file_path)

    def test_read_line(self):
        with open('demo.txt') as file_handler:
            for line in read_line(file_handler):
                self.assertTrue(line.startswith('Wilt'))
                break

    def test_word_count(self):
        result = word_count('demo.txt', 'and,it')
        self.assertEqual(result[0], ('the', 22))
