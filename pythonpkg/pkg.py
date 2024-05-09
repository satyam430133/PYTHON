import random
li = []
def CreateList(li,n):
    for i in range(n):
        num = random.randint(0,100)
        li.append(num)
    return li
    
def demo():
    print("Ash")
# a = CreateList([],5)
# print(a)
# print("okay done")