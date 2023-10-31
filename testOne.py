# test_total_books1.py
import unittest
from my_program import total_books

class TestTotalBooks(unittest.TestCase):
    def test_total_books(self):
        self.assertEqual(total_books(7, 3), 21)

if __name__ == '__main__':
    unittest.main()