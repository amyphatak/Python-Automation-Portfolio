#self keyword is manadatory for calling varaible name
#constructor name should be __init__
#instance varaibles keep changing for every object creation but class varaiables does not change

class Calculator:
     num = 100 # class varaibales are constant no mater how many objects will be created
     # constructor is a method which is automatically called when any object is created
#default constructor
     def __init__(self,a,b):
         self.firstNumber = a
         self.secondnumber = b
         print("I am called automatically when object is created")


     def getData(self):
         print("I am now executing as a method in class")

     def Summation(self):
         return self.firstNumber + self.secondnumber + self.num


obj = Calculator(2,3) # sntax to create obj in python
obj.getData()
print(obj.Summation())

obj1 = Calculator(4,5) # sntax to create obj in python
obj1.getData()
print(obj1.Summation())


class BasicCalculator:
     def __init__(self,a,b):
         self.firstNumber = a
         self.secondnumber = b

     def Addition(self):
         return self.firstNumber + self.secondnumber
     def Subtraction(self):
         return self.firstNumber - self.secondnumber
     def Multiplication(self):
         return self.firstNumber * self.secondnumber
     def Division(self):
         self.firstNumber / self.secondnumber

obj = BasicCalculator(10,5)
print("Addition:",obj.Addition())
print("Subtraction:",obj.Subtraction())
print("Multiplication:",obj.Multiplication())
print("Division:",obj.Division())