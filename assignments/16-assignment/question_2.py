"""
2. Create a class Product with members as pid,pname,price and quantity .Add 
following methods:  
e.  Constructor (Support both parameterized and parameterless)  
f. Destructor   
g.  ShowBook  
h.  Add static member discount.  
i. Provide methods for applying discount on price of product.
"""

class Product:

    discount = 10
    def __init__(self, pid = None, pname = None, price = 0, quantity = 0):
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

    def discountOnProduct(self):
        discount_amount = (self.price * Product.discount) /100
        final_price = self.price - discount_amount
        print(f'Final price of the product after applying discount is {final_price}.')

    def __del__(self):
        print('Destructor is created after complition of Object lifespan.')

product = Product(1235, 'Himalaya Face Cream', 399, 1)
print(product.showProduct())
product.discountOnProduct()
print('------------------------------------------------------------------')
