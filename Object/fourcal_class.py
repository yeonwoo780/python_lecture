class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

a = FourCal(4, 2)
b = a.add()
print(b)