# String
# s = "apple is good for health"
# print(s)
# print(s.upper())
# print(s.replace('a',"k"))
# WAP To count mumber of alphabet, digit, special character, upper letters, lower letter in a string 
s = "india is GREAT !!! 12345"
uprcase = 0
lwrcase = 0
digit = 0
special = 0
for i in s:
    if i.islower():
        lwrcase = lwrcase + 1
    elif i.isupper():
        uprcase = uprcase +1
    elif i.isdigit():
        digit = digit + 1
    else:
        special = special + 1
print("Uppercase = ",uprcase,"lowercase = ",lwrcase,"Digit = ",digit,"Speacial Character =",special)