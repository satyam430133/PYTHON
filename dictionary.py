d = {1:"jerry",2:"sharry",3:"harry"}
'''
# Methods of Dictionary 
# keys(),values(),items()
for i in d:
    print(i)    # print the key of dictionary 
    print(d[i]) # print object of dictionary
    print(d[2]) # print object of dictionary
k = d.keys() # special fuction store the keys in a single object
v = d.values() # special fuction store the values in a single object
print(k) 
print(v)
print(type(k))
print(type(v))
print("===================================")
for i in d.values():
    print(i) 
'''  
# for i in d.items():
#     print(i)
# for i,j in d.items(): # for loop using two variable is called packing and unpacking 
#     print(i,j)

# lis= [[1,2,"a"],[3,4,"b"],[5,6,"c"],[7,8,"d"]]
# for i in lis:
#     print(i)
# for i,j,k in lis:
#     print(i,j,k) 
# # update() setdefault() get()
# print("=============================================")
# print(d.get(3))
# print(d.get(40)) # if key does'nt exist then it will return none in answer 
# print(d.get(60,"Value Does not Exist")) # if there is no value related then we can also return massage or none or other things 
d1 = {4:"cherry",5:"kerry"}
d.update(d1)
print(d)
print(d.update({2:"shyamlal"})) # update the dictionary in dictionary 
print(d)  