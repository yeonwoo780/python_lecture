def print_sum():
    global a, b # 변수값을 고정 시켜줌 밖에서 바꿀수 없음
    a = 100
    b = 200
    result = a + b
    print('print_sum() 내부 : {} 와 {}의 합은 {}다.\n'.format(a, b, result))

a = 10
b = 20
print_sum()
result = a + b
print('print_sum() 외부 : {} 와 {}의 합은 {}다.\n'.format(a, b, result))