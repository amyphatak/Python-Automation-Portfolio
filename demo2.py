values= [1, 2, "rahul", 4, 5]
print(values[0]) #print 1
print(values[-1])
print(values[-4])
print(values[1:3])
values.insert(3,"phatak")
print(values)
values.insert(4,"test")
print(values)
values.insert(1,2)
print(values)
values.append(4)
print(values)
del values[0]
print(values)

Val= [1,2,"rahul",4.5]
print(Val[1])
Val[2]="RAHUL"
print(Val)

dic = {"a":2, 4:"bc", "d":5}
print(dic[4])
print(dic["a"])