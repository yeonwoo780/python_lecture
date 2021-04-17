class FourCal:
    ##부모노드. 아들껄 쓰지못한다. 
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

class FourCal_div(FourCal):
    ## 자식노드. 부모껄 상속받는다 오버라이딩
     def div(self):
         result = self.first / self.second
         return result

div_data = FourCal_div(4,2)         
a = div_data.div()
print(a)