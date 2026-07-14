# print first three characters and last three characters of string

s= "Wonderful"
if len(s)< 6 :
    print("")
else:
    new_string = s[:3]+s[len(s)-3:]
    print(new_string)

s= "Blue"
if len(s)< 6 :
    print("")

s= "Amazing"
if len(s)<6:
    print("")
else:
    new_string = s[:3]+ s[len(s)-3 :]
    print(new_string)

#option 2
s= "wonder"
num_chars= 4
if len(s) < num_chars*2:
    print("")
else:
    new_string = s[:num_chars]+ s[len(s)-num_chars:]
    print(new_string)



s = "beautiful"
if len(s)<8:
    print("")
else:
    new_string = s[:4] + s[len(s)-4:]
    print(new_string)



