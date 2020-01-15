# -*- coding: utf-8 -*-
from Book import Book
#First Book is file & second is Class

class Catalog:
    def __init__(self):
        self.different_book_count = 0
        self.books = []

#Only available to admin
    def addBook(self,name,author,publish_date,pages):
        b = Book(name,author,publish_date,pages)
        self.different_book_count += 1
        self.books.append(b)
        return b

        #Only available to admin
    def addBookItem(self,book,isbn,rack):
        book.addBookItem(isbn, rack)


    def searchByName(self,name):
        for book in self.books:
            if name.strip() == book.name:
                return book

    
    def searchByAuthor(self,author):
        for book in self.books:
            if author.strip() == book.author:
                return book

    def displayAllBooks(self):
        print ('Different Book Count',self.different_book_count)
        c = 0
        for book in self.books:
            c += book.total_count
            book.printBook()    
        print ('Total Book Count',c)
        
    def RequestBook(self,name):
        print("Please enter name of the Book you need to take:")
        self.Book=input()
        return self.Book
    
    def returnBook(self,name):
        print("please enter the name of Book you want to return:")
        self.Book=input()
        return self.Book
    
    def removeBookItemFromCatalog(self,requestedBook):
            if requestedBook in self.Book:
                  print("The book you requested has now been borrowed")
                  self.Book.remove(requestedBook)
            else:
                  print("Sorry the book you have requested is currently not in the library")

    def removeBookItem(self,name,isbn):
        book = self.searchByName(name)
        book_item = book.searchBookItem(isbn)
        book.removeBookItem(book_item)
        
class Student:
    #assume name is unique
    def RequestBook(self,name):
        self.name = name
        print("Enter the name of the book you'd like to borrow>>")
        self.Book=input()
        return self.Book
    
    #assume name is unique
    def returnBook(self,name):
        self.name = name
        print("Enter the name of the book you'd like to return>>")
        self.Book=input()
        return self.Book

class Library:
    def __init__(self,listofbooks):
        self.displayAllbooks = listofbooks
 