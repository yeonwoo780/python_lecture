class Calculator:
    def __init__(self, num=0):
        self.result = num ## default 값 0

    def add(self, num):
        self.result += num ## add num    init result
        return self.result

cal = Calculator()
data = cal.add(5)
print(data)

cal1 = Calculator(3)
data = cal1.add(5)
print(data)