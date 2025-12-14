"""
3. Create a class Shirt  with members as sid,sname,type(formal etc), price and 
size(small,large etc) .Add following methods:  
g.  Constructor (Support both parameterized and parameterless)  
h.  Destructor   
i. ShowBook
"""

class Shirt:
    def __init__(self, sid, sname, stype, price, size):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.price = price
        self.size = size

    def showShirt(self):
        return f""""
        SHIRT_ID: {self.sid}
        SHIRT_NAME: {self.sname}
        SHIRT_TYPE: {self.stype}
        SHIRT_PRICE: {self.price}
        SHIRT_SIZE: {self.size}
        """

    def __del__(self):
        print('Destructor is called.')

shirt = Shirt(132, 'SiyaRam', 'Formal', 1200, 'Medium')
print(shirt.showShirt())