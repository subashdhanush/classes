class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"📚 '{book_name}' added to the library.")

    def borrow_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"📖 You borrowed '{book_name}'.")
        else:
            print(f"❌ '{book_name}' is not available.")

    def return_book(self, book_name):
        self.books.append(book_name)
        print(f"🔄 '{book_name}' returned to the library.")

    def display_books(self):
        print("📚 Available books:", self.books)


# Creating a Library object
lib = Library()
lib.add_book("Python Basics")
lib.add_book("Data Science")
lib.display_books()

lib.borrow_book("Python Basics")
lib.display_books()

lib.return_book("Python Basics")
lib.display_books()
