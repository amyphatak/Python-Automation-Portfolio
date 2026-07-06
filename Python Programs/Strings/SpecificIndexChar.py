# print the character at specific index

s = "Hell0" #len = 5 #index= 4
i=0

if not s: # use if not s --> Clean way to find empty string
    print("Empty String")
elif i<len(s):
    print(s[i])
else:
    print("index out of range")

