"""
1. Create a class Book with members as bid,bname,price and author.Add following 
methods:  
a.  Constructor (Support both parameterized and parameterless)  
b.  Destructor   
c.  ShowBook  
d.  Add static variable count and also maintain count of objects created.
"""

class Book:

    count = 0
    def __init__(self, bid, bname, price, author):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

        Book.count += 1

    def showBook(self):
        return f"""
        BOOK_ID: {self.bid}
        BOOK_NAME: {self.bname}
        BOOK_PRICE: {self.price}
        BOOK_AUTHOR: {self.author}    
        """

    def __del__(self):
        print('This is destructor.')

book = Book(101, 'Gunhao ka Devta', 200, 'Dharmveer Bharti')
book1 = Book(101, 'Gunhao ka Devta', 200, 'Dharmveer Bharti')

print(book.showBook())
print(book1.showBook())
print(Book.count)