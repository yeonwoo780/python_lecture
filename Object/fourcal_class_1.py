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

a = FourCal(1,2)         
print('두수의 합은 : {}\n'.format(a.add()))
print('두수의 곱은 : {}\n'.format(a.mul()))
print('두수의 빼기은 : {}\n'.format(a.sub()))  
print('두수의 나누기는 : {}\n'.format(a.div()))

a1 = FourCal_1()         
print('두수의 합은 : {}\n'.format(a1.add()))
print('두수의 곱은 : {}\n'.format(a1.mul()))
print('두수의 빼기은 : {}\n'.format(a1.sub()))  
print('두수의 나누기는 : {}\n'.format(a1.div()))