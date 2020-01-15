  # -*- coding: utf-8 -*-

from Book import Book
from Catalog import Catalog
from User import Member, Librarian

b1 = Book('python','py', '2015',312)
b1.addBookItem('123A','H1B2')
b1.addBookItem('124B','H1B3')

b1.printBook()

catalog = Catalog()

b = catalog.addBook('python','py', '2015',312)
catalog.addBookItem(b, '123hg','H1B2')
catalog.addBookItem(b, '124hg','H1B4')
catalog.addBookItem(b, '125hg','H1B5')

b = catalog.addBook('Einstien','J ', '2017',318)
catalog.addBookItem(b, '463hg','K1B2')

b = catalog.addBook('C','E Balguruswamy', '1985',319)
catalog.addBookItem(b, '473A','K1B3')

b = catalog.addBook('Verses','Walker', '2011',320)
catalog.addBookItem(b, '483B','K1B4')

catalog.displayAllBooks()

m1 = Member("pavan","hassan",23,'asljlk@j22','std1233')

librarian = Librarian("veeresh", "Bangalore",24,'asljlk@j32', 'zeke101') 
print (m1)
print (librarian)

b = catalog.searchByName('python')
print (b)

b = catalog.searchByName('C')
print (b)

b = catalog.searchByAuthor('dennis')
print (b)

#catalog.removeBookItem('Shoe Dog','124hg')
#catalog.displayAllBooks()
#m1.issueBook

b = catalog.RequestBook("")
print (b,"Book issued Successfully")

b = catalog.returnBook('')
print (b,"Book returned Successfully Thank you")
