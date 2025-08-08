class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"'{self.title}' by {self.author} has got at least {self.pages} pages"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"

book1 = Book("1984", "George Orwell", 328)
book2 = Book("Siku Njema", "Ken Walibora", 250)

print(str(book1))
print(repr(book1))
print(str(book2))
print(repr(book2))