class BasicCalcularor:
      def __init__(self,a,b):
            self.Firstnum = a
            self.Secondnum = b

      def Addition(self):
          return self.Firstnum +self.Secondnum
      def Subtraction(self):
          return self.Firstnum -self.Secondnum
      def Multiplication(self):
          return self.Firstnum *self.Secondnum
      def Division(self):
          return self.Firstnum / self.Secondnum


obj= BasicCalcularor(10,5)
print("Addition:", obj.Addition())
print("Subtraction:", obj.Subtraction())
print("Multiplication:", obj.Multiplication())
print("Division:", obj.Division())


def CalculateAverage(num1, num2, num3):
    return (num1 + num2 + num3) / num3


avg = (10, 20, 30)
print("The average of 10,20 and 30 is 20.0")