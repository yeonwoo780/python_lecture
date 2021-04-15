def div(a = 1, b = 2): #default 값 1, 2
    return a / b

print('div() =', div()) # 인자가 없을 경우 div(1, 2)로 간주
print('div(4) =', div(4)) # div(4, 2)로 간주함
print('div(6, 3) =', div(6, 3))