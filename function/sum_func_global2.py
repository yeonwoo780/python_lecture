def print_sum():
    a = 100
    b = 200
    result = a + b
    print('print_sum() 내부 : {} 와 {}의 합은 {}다.\n'.format(a, b, result))

a = 10
b = 20
print_sum()
result = a + b
print('print_sum() 외부 : {} 와 {}의 합은 {}다.'.format(a, b, result))