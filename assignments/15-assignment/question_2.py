"""
2. Create a class Product with members as pid,pname,price and quantity .Add 
following methods:  
d.  Constructor (Support both parameterized and parameterless)  
e.  Destructor   
f. ShowProduct 
"""

class Product:
    def __init__(self, pid, pname, price, quantity):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def showProduct(self):
        return f"""
        PRODUCT_ID: {self.pid}
        PRODUCT_NAME: {self.pname}
        PRODUCT_PRICE: {self.price}
        PRODUCT_QUANTITY: {self.quantity}
        """

    def __del__(self):
        print('Destructor is called.')

product = Product(1235, 'Himalaya Face Cream', 399, 1)
print(product.showProduct())