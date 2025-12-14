"""
3. Create a class Shirt  with members as sid,sname,type(formal etc), price and 
size(small,large etc) .Add following methods:  
j. Constructor (Support both parameterized and parameterless)  
k.  Destructor   
l. ShowBook  
m. For each size of shirt price should change by 10%. 
(eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and 
xlarge=1300) Use static concept.
"""

class Shirt:
    shirt_size = {
        'small' : 0,
        'medium' : 10,
        'large' : 20,
        'xlarge' : 30
    }
    def __init__(self, sid=None, sname=None, stype=None, sprice=0, size='small'):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.sprice = sprice
        self.size = size

    def showShirt(self):
        return f""""
        SHIRT_ID: {self.sid}
        SHIRT_NAME: {self.sname}
        SHIRT_TYPE: {self.stype}
        SHIRT_PRICE: {self.sprice}
        SHIRT_SIZE: {self.size}
        """

    def calculatePrice(self):
        increase_percent = Shirt.shirt_size.get(self.size, 0)
        increase_aoumnt = (self.sprice * increase_percent) / 100
        return f'FINAL PRICE: {self.sprice + increase_aoumnt}'

    def __del__(self):
        print('Destructor is called.')

shirt = Shirt(132, 'SiyaRam', 'Formal', 1200, 'medium')
print(shirt.showShirt())
print(shirt.calculatePrice())