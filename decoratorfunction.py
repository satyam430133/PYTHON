# Decorator, Wrapper 
# -> It enhance the functionality of existing function. 
# -> In decorator we define the function inside the body of function 
def wrapper(add):
    def arthmetic(a,b):
        add(a,b)
        print("Substraction",a-b)
        print("Division",a/b)
        print("Product",a*b)
    return arthmetic

@wrapper
def add(a,b):
    print("ADD",a+b)

add(4,5)
def deco(createList):
    def swapper(lis):
        createList(lis)
        lis[0], lis[-1] = lis[-1], lis[0]
    return swapper
@deco
def createList(lis):
    for i in range(10):
        lis.append(i)
    print(lis)
lis = []
createList(lis)
print(lis)

def evodd(a):
    if a % 2 == 0:
        return "even"
    else:
        return "odd" 

l = [2, 54, 56, 6, 85, 4, 6, 8]
result = list(filter(evodd, l))
print(result)

def evodd(a):
    if a % 2 == 0:
        return True

lis = [2, 3,5, 56, 6, 85, 4, 6, 8]
result = list(filter(evodd, lis))
print(result)