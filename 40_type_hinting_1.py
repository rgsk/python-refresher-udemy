from typing import List


class Book:
    TYPES = ('handcover', 'paperback')

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight) -> "Book":
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight) -> "Book":
        # we can use Book too, but using cls is better
        return Book(name, Book.TYPES[1], page_weight)


class BookShelf:
    def __init__(self, *books: Book) -> None:
        self.books = books

    def __str__(self) -> str:
        return f"BookSelf with {len(self.books)} books."


book1 = Book.hardcover('Harry Potter', 1500)
print(book1)
book2 = Book.paperback('Harry Potter', 1800)
print(book2)

shelf1 = BookShelf(book1, book2)
print(shelf1)
