file=open('test.txt')
#readall contents of the file
print(file.read(2))
line=file.readline()
while line!="":
    print(line)
    line = file.readline()



file.close()