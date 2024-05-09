''' 
WAP to create a list of n elements with the help of function & also find the maximun and the minimun element in the list. 
Parameter contain Empty list and the number N OUTPUT = List, Minimun Value, Maximun Value 
'''
import random
import math
n = int(input("Enter N Number"))
lis = []
def createList(lis, n):
    for i in range(n):
        num = random.randrange(2, 100, 3)s
        lis.append(math.floor(num))
    return lis,max(lis),min(lis),"Thank You"
a = createList(lis,n) # Return the value in the form of touple
print(a)