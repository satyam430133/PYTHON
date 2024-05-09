# with open("apple.txt","a") as f:
#     while True:
#         data = (input("Enter Content"))
#         f.write(data+"\n")
#         n = input("Enter N for exit")
#         if n in 'nN':
#             print("data Inserted")
#             break

# to read in single line or multiple lines 
        # data = f.readlines()
        # print(data)

# f.tell() define the position of the pointer 
# f.seek() changes the position of the pointer 
with open("apple.txt","r") as f:
    print(f.tell())
    a = f.readline()
    print(a)
    print(f.tell())
    f.seek(0)
    b = f.readline()
    print(b)
