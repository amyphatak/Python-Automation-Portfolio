class Calculator:
    num =100
    #defalut constructor
    def __init__(self,a,b):

        self.firstnumber = a
        self.secondnumber = b
        print("I am called utomatically when object is created")

    def getData(self):
        print("I am now executing as a method in class")

    def Summation(self):
        return self.firstnumber + self.secondnumber +self.num

obj =Calculator(2,3)
obj.getData()
print(obj.Summation())




