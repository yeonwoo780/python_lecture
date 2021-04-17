class FourCal:
     def __init__(self, first, second):#propoty=2 method=4
         self.first = first
         self.second = second

     def add(self):
         result = self.first + self.second
         return result

     def mul(self):
         result = self.first * self.second
         return result

     def sub(self):
         result = self.first - self.second
         return result

     def div(self):
         result = self.first / self.second
         return result

class FourCal_1(FourCal):
    def __init__(self, first = 0, second = 0):#propoty=2 method=4
         self.first = int(input("first : "))
         self.second = int(input("second : "))
