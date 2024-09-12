class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author
    self.available = True

  def checkout(self):
    if self.available == True:
      self.available = False
      return True
    if self.available == False:
      return False
  
  def return_book(self):
    self.available = True
  
  def display_info(self):
    print(f"---\nBook Title: {self.title}\nAuthor: {self.author}\nAvailable Status: {self.available}\n---")

book1 = Book("The Secret", "Rhonda Byrne")
book2 = Book("Tentang Kamu", "Tere Liye")
book3 = Book("Sapiens: A Brief History of Humankind", "Yuval Noah Harari")

class Library(Book):
  def __init__(self):
    self.books = []
  
  def add_book(self, book):
    self.books.append(book)
  
  def display_books(self):
    for book in self.books:
      book.display_info()

  def get_book_by_title(self, title):
    for book in self.books:
      if book.title.lower() == title.lower():
        return book
    return None

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.display_books()

search_title = "The Secret"
found_book = library.get_book_by_title(search_title)

if found_book:
    print(f"Book found!")
    found_book.display_info()
else:
    print(f"There are no books with the title: {search_title}")