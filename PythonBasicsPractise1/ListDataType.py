values = [1,2,"Rahul",4,5]# list should be in square bracket, allows multiple value can be with different datatype
print(values[0])

print(values[3])
print(values[-1])
print(values[1:3])
values.insert(3,"shetty")
print(values)
values.append(6)
print(values)

values[2]=("RAHUL")#UPDATING
del values[0]
print(values)
