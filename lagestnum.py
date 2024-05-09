my_list = [10, 5, 20, 15, 8]


max_num = my_list[0]

for num in my_list[1:]:
    if num > max_num:
        max_num = num

print("The largest number in the list is:", max_num)
