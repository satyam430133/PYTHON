# instance variabel 
# class variable

class Circle:
    a = 50
    def __init__(self,r):
        self.rad = r
    def area(self):
        print("Area:-", 3.141 * self.rad * self.rad)
    def perimeter(self):
        print("Perimeter:-", 2 * 3.141 * self.rad)

zx = Circle(5)
xz = Circle(4)