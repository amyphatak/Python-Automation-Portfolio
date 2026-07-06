# Inheritance : Acquiring properties of parent class
from OOPSDemo import Calculator


class childImp(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self,2,10) # child and Parent

    def getcompleteData(self):
        return self.num2+ self.num + self.Summation()


obj =childImp()
obj.getcompleteData()
print(obj.getcompleteData())

