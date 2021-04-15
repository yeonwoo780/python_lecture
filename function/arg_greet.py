def greet(*names):
    for name in names:
        print('hi', name,'!\n')

greet('Peter','John','Pen') # 인자 3개
greet('James', 'Thomas') # 인자 2개