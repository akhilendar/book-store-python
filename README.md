# Book Store Application

## Overview

This is a simple Book Store application written in Python. The application allows users to add books, view all books, search for books by title or author, and delete books. It is designed for educational purposes to help candidates practice their Python and software development skills.

## Folder Structure

```
book-store/
├── src/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── book.py
│   ├── app.py
├── tests/
│   ├── __init__.py
│   ├── test_book_store.py
├── requirements.txt
├── README.md
```

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/book-store.git
   cd book-store
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

To run the Book Store application, execute the following command:

```bash
python src/app.py
```

### Using the Application

1. **Add a Book:**

   - Follow the prompts to enter the book title, author, ISBN, and price.

2. **View All Books:**

   - Displays the list of all books available in the store.

3. **Search Books:**

   - You can search for books by title or author.

4. **Delete a Book:**

   - Enter the ISBN of the book you wish to delete.

5. **Exit:**
   - Exit the application.

### Running Tests

To run the unit tests for the application, execute the following command:

```bash
python -m unittest discover tests
```

## Project Structure

- `src/models/book.py`: Contains the `Book` class which defines the structure of a book.
- `src/app.py`: Contains the main logic for the Book Store application.
- `tests/test_book_store.py`: Contains unit tests for the Book Store application.

## Example

```python
# Example of adding a book
book = Book("1984", "George Orwell", "1234567890", 15.99)
store.add_book(book)

# Example of viewing all books
store.view_books()

# Example of searching for a book by title
store.search_books(title="1984")

# Example of deleting a book
store.delete_book("1234567890")
```

## Existing Implementation

### Models

#### `src/models/book.py`

Defines the `Book` class with the following attributes:

- `title`: The title of the book.
- `author`: The author of the book.
- `isbn`: The ISBN number of the book.
- `price`: The price of the book.

Example:

```python
class Book:
    def __init__(self, title, author, isbn, price):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price

    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.isbn}, {self.price})"
```

### Application Logic

#### `src/app.py`

Implements the main logic for the Book Store application, including:

- Adding a book
- Viewing all books
- Searching for books by title or author
- Deleting a book
