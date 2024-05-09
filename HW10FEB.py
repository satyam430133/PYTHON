#d = {1:"monday",2:"tuesday",3:"wednesday",4:"thursday",5:"friday",6:"saturday",7:"sunday"}
d1 = {1:"monday",2:"tuesday",3:"wednesday",6:"saturday",7:"sunday"}
'''
for i in d1:
    if i == 2:
        print("jai")
        # d1.update({4:"thursday",5:"friday"})
    else:
        continue
print(d1)
'''

d2 = {23:"ajay",32:"vijay",-1:"vijay"}
if d2.keys(23) > d2.keys(32)
    d2[0],d2[1] = d2[1],d2[0]
print(d2)
# for i in d2:
#     if d2[i] > d2[i+1]:
#         d2[i],d2[i+1] = d2[i+1],d2[i]
#     else:
#         continue
# print(d2)