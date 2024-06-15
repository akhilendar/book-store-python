import unittest
from src.models.book import Book
from src.app import BookStore


class TestBookStore(unittest.TestCase):

    def setUp(self):
        self.store = BookStore()

    def test_add_book(self):
        book = Book("Test Title", "Test Author", "1234567890", 10.99)
        self.store.add_book(book)
        self.assertIn(book, self.store.books)

    def test_view_books(self):
        book = Book("Test Title", "Test Author", "1234567890", 10.99)
        self.store.add_book(book)
        self.assertEqual(self.store.books, [book])

    def test_search_books_by_title(self):
        book = Book("Test Title", "Test Author", "1234567890", 10.99)
        self.store.add_book(book)
        results = self.store.search_books(title="Test Title")
        self.assertIn(book, results)

    def test_search_books_by_author(self):
        book = Book("Test Title", "Test Author", "1234567890", 10.99)
        self.store.add_book(book)
        results = self.store.search_books(author="Test Author")
        self.assertIn(book, results)

    def test_delete_book(self):
        book = Book("Test Title", "Test Author", "1234567890", 10.99)
        self.store.add_book(book)
        self.store.delete_book("1234567890")
        self.assertNotIn(book, self.store.books)


if __name__ == "__main__":
    unittest.main()
