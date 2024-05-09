class book:
    def __init__(self,n,bid,q):
        self.name = n
        self.bid = bid
        self.quantity = q
    def purchase(self,qty):
        self.quantity += qty
    def sale(self,qty):
        self.quantity -= qty
    def display(self):
        print("Book Name : ",self.name)
        print("Book ID : ",self.bid)
        print("Book Quantity : ",self.quantity)

# zx = book("Python",1245748,50)
# zx.display()
# zx.purchase(527)
# zx.display()
# zx.sale(227)
# zx.display()
class library(book):
    pass

x = library("asjsh",654,55)
x.display()