class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author 


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        if isinstance(book, list):
            self.books.extend(book)
        else:
            self.books.append(book)

    def remove_book(self, book):
        print(self.books)
        for word in book:
            word.lower()
            if word in self.books():
                self.books.remove(book)

    def search_books(self, search_string):
        buuohui