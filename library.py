# 2 classes library and student
class library:
    def __init__(self, listofbooks):
       self.availableBooks = listofbooks

    def displayAvailableBooks(self):
        print("Books that we have rigth now")
        for book in self.availableBooks:
            print(book)
            
    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print('you have borrowed it')
        else:
            print('sorry')
    def addBook(self,returnBook):
        self.returnBook = returnBook
        return print(f'you returned this {self.returnBook}')

     
    

class student:
    def requestBook(self):
        print('enter the book you would like to borrow')
        self.book = input()
        return self.book

    def returnBook(self):
        print('enter the book you would like to return')
        self.book = input()
        return self.book
    

def main():            
    Library = library(['book1','book2','book3'])
    Student = student()
    done = False
    while done == False:
        print("""======Library Menu=====
            1. Display available books
            2. Request a book
            3. Return a book
            4. Exit  
            """)
        choice = input('Enter a choice : ')
        if choice == '1':
            Library.displayAvailableBooks()
        elif choice == '2':
            Library.lendBook(Student.requestBook())    
        elif choice == '3':
            Library.addBook(Student.returnBook())
        elif choice == '4':
             print('thank you') 
             break      


main()