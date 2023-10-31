# test_total_books2.py
import unittest
from my_program import total_books

class TestTotalBooks(unittest.TestCase):
    def test_total_books(self):
        self.assertEqual(total_books(5, 4), 20)

if __name__ == '__main__':
    unittest.main()