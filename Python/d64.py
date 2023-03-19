# Library Management SYstem

'''
Write a library class with no_of_books and books as 2 instance variable.
Write a program to create a library from this library class and show how you can print all books,add a book and get the number of books.
Show that your program doesn't persist the books after the program is stopped.

'''

class Library:
    def __init__(self):
        self.nBooks=0
        self.books=[]

    def addBook(self,book):
        self.books.append(book)
        self.nBooks=len(self.books)

    def showInfo(self):
        print(f"The library has {self.nBooks} books.The books are:")
        for i in self.books:
            print(i)

l1=Library()
l1.addBook("Rich Dad Poor Dad")
l1.addBook("Think like a monk")
l1.addBook("Atomic Habits")
l1.addBook("The Invisible man")

l1.showInfo()





