class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def check_out(self):
        pass
    def return_book(self):
        pass
    def is_available(self):
        return not self._is_checked_out

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)
    
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book._is_checked_out = True
                return f"{title} has been checked out."
        return f"{title} is not available for checkout."
    
    def return_book(self, title):
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book._is_checked_out = False
                return f"{title} has been returned."
        return f"{title} was not checked out."
    
    def list_available_books(self):
        available_books = [book.title for book in self._books if not book._is_checked_out]
        return available_books if available_books else "No books are currently available."