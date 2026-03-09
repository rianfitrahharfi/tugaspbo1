import unittest

class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def discount(self, disc):
        return self.price - disc


class TestBook(unittest.TestCase):

    def test_discount(self):
        book = Book("Python", 100)
        result = book.discount(20)
        self.assertEqual(result, 80)


if __name__ == "__main__":
    unittest.main()