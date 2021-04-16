class Cat:
    def __init__(self, name, color="흰색"): #초기화 함수
        #self시작점(a,b나 아무변수명 가능) 나머진 매개변수 이용
        self.name = name
        self.color = color

    def meow(self):
        print('내 이름은 {}, 색깔은 {}, 야옹 야옹'.format(self.name, self.color))
    
nabi = Cat("나비") #self.name = 나비 #self.color = default
nabi.meow()

nero = Cat("네로","블루")
nero.meow()

mimi = Cat("미미","퍼플")
mimi.meow()