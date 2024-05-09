# WAP to find the average of n numbers with the help of funtion which named Add()
def add(n):
    sum = 0
    for i in range(n):
        num = int(input("Enter Values"))
        sum = sum + num
    return sum
n = int(input("Enter Range"))
a = add(n)
avg = a/n
print(avg)