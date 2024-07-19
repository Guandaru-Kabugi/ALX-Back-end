#class Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"{self.title} by {self.author}"
    
book1 = Book("Start with WHY", "Simon Sinek")
book2 = Book("The Alchemist", "Paulo Coelho")
book3 = Book("Pride and Prejudice", "Jane Austen")
books = [book1,book2, book3]
print([str(book) for book in books] )
print()
#class Member
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
        self.member_card = []
    def add_borrowed_books(self, book):
        self.borrowed_books.append(book)
    def member_card_add(self, card):
        self.member_card.append(card)
    @staticmethod
    def member_fine(fine_per_day,overdue_days):
        if overdue_days == 0:
            return None
        elif overdue_days < 0:
            raise ValueError("Overdue days cannot be less than zero")
        else:    
            fine = fine_per_day * overdue_days
            return fine
    def __str__(self):
        return f"Member_Name: {self.name}, Card Number: {[int(number) for number in self.member_card]}, Borrowed_Books: {[str(book) for book in self.borrowed_books]}"
member1 = Member("Alex")
member2 = Member("James")
member1.member_card_add(2342123344)
member2.member_card_add(3431783627)
member2.member_card_add(3910726383)
member1.add_borrowed_books(book1)
member2.add_borrowed_books(book2)
member2.add_borrowed_books(book3)
print(f"{member2} fine is {member2.member_fine(100, 0)}")
print(f"{member1} fine is {member1.member_fine(100, 3)}")
print()
print(member1)
print(member2)
#class Library
class Library:
    lib_slogan = "Welcome to ALX Library"
    total_borrowed_books = 0
    total_members = 0
    
    def __init__(self, name):
        self.name = name
        self.bookobject = []
        self.memberobject = []
    def add_book_object(self, book):
        self.bookobject.append(book)
        Library.total_borrowed_books+=1
    def member_objects(self, member):
        self.memberobject.append(member)
        Library.total_members+=1
    @classmethod
    def library_slogan(cls):
        return Library.lib_slogan
    def __str__(self):
        return f"Library SLogan: {Library.library_slogan()}, Library Name: {self.name}, Books: {[str(book) for book in self.bookobject]}, Members: {[str(member) for member in self.memberobject]}"
library1 = Library("ALX CPA HUB")
book3 = Book("Title 3", "Author 3")
library1.add_book_object(book1)
library1.add_book_object(book2)
library1.add_book_object(book3)
library1.member_objects(member2)
library1.member_objects(member1)

print()
print(library1)