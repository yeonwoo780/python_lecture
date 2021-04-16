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

x = int(input('첫번째 숫자'))
y = int(input('두번째 숫자'))
a = FourCal(x, y)

print('두수의 합은 : {}\n'.format(a.add()))
print('두수의 곱은 : {}\n'.format(a.mul()))
print('두수의 빼기은 : {}\n'.format(a.sub()))  
print('두수의 나누기는 : {}\n'.format(a.div()))
