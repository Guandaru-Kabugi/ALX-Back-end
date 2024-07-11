class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False
        
class Library():
    
    def __init__(self):
        self._books = []
        self._checked_out_books = []
    def add_book(self, book):
        self._books.append(book)
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book.check_out()
                self._books.remove(book)
                self._checked_out_books.append(book)
                
    def return_book(self,title):
        for book in self._checked_out_books:
            if book.title == title and book._is_checked_out:
                book.return_book()
                self._checked_out_books.remove(book)            
                self._books.append(book)
    def list_available_books(self):
        for book in self._books:
            print(f"{book.title} by {book.author}")