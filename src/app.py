from src.models.book import Book


class BookStore:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully.")

    def view_books(self):
        if not self.books:
            print("No books available.")
        else:
            for book in self.books:
                print(book)

    def search_books(self, title=None, author=None):
        results = []
        if title:
            results = [book for book in self.books if title.lower()
                       in book.title.lower()]
        elif author:
            results = [book for book in self.books if author.lower()
                       in book.author.lower()]

        if not results:
            print("No books found.")
        else:
            for book in results:
                print(book)

    def delete_book(self, isbn):
        book_to_delete = None
        for book in self.books:
            if book.isbn == isbn:
                book_to_delete = book
                break

        if book_to_delete:
            self.books.remove(book_to_delete)
            print(f"Book '{book_to_delete.title}' deleted successfully.")
        else:
            print("Book not found.")


def main():
    store = BookStore()
    while True:
        print("\nBook Store Menu:")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Delete Book")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            price = input("Enter book price: ")
            book = Book(title, author, isbn, price)
            store.add_book(book)
        elif choice == '2':
            store.view_books()
        elif choice == '3':
            search_choice = input("Search by title or author? (t/a): ")
            if search_choice == 't':
                title = input("Enter title: ")
                store.search_books(title=title)
            elif search_choice == 'a':
                author = input("Enter author: ")
                store.search_books(author=author)
        elif choice == '4':
            isbn = input("Enter ISBN of the book to delete: ")
            store.delete_book(isbn)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
