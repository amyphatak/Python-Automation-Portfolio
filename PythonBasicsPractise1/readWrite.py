file = open('Test.txt')
#all contents of file
#read n number of character by passing parameter
#read one single line at a time using readline() method
#print(file.read(2))
#print(file.readline())
file.close()

#print line by line using readline method

#line=file.readline()
#while line!="":
  #  print(line)
  #  line = file.readline()


#values = [abc, bvdsf, "cat", dog, elephant]
for line in file.readlines():
    print(line)