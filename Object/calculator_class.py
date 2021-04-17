class Calculator:
    def __init__(self, num = 0):
        self.result = num ## default 값 0

    def add(self, num):
        print("{} + {}".format(self.result,num))
        self.result += num ## init result + num
        return self.result

cal = Calculator()
data = cal.add(5)
print(data)

cal1 = Calculator(3)
data = cal1.add(5)
print(data)