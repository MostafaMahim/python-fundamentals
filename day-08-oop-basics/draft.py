class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def summary(self):
        # "'Atomic Habits' by James Clear, 320 pages"
        return f"'{self.title}' by {self.author}, {self.pages} pages"
    def is_long(self):
        if self.pages > 500 :
            return True
        else:
            return False


book1 = Book("Learn Physcis","Mostafa M", 200)
print(book1.summary())
print(book1.is_long())
book2 = Book("30 Days Match","Masrukh ak", 600)
print(book2.summary())
print(book2.is_long())