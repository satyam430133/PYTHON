# Program for multiple value return
a = int(input("Enter Value of a"))
b = int(input("Enter Value of b")) 
def arithmetic(a,b):
    return a+b,a-b, a*b, a/b
add,sub,multi,div = arithmetic(a,b) # this is called multiple assignment
print(add,sub,multi,div)


def f1(l):
    for i in range(3):
        l.append(i)
        return(l) # function terminate kar deta hai break statement ki tarah 
a = f1([])
print(a)