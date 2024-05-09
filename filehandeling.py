# File Handeling 
# write(), writelinees()
# read(), readline(), readlines()
# w for write, a for append, r for read
#    with open ("apple.txt","w") as f #block # way to open file isme file close karne ki jarurat nahi hoti hai 

f = open("apple.txt","a") 
a = "Apple is good for health  "
b = "Banana is good for health "
c = "Thank You "
f.write(a)
f.write(b)
f.write(c)
f.close()
print("Data Updated Successfully")
