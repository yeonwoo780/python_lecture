def factorial(n): ## n!
    if n <= 1: # 1!은 1이므로 
        return 1
    else:
        return n * factorial(n - 1) # 2*1, 3*2*1, 4*3*2*1 ... n*n-1...*1

n = 5
print('{}! ? : {}'.format(n, factorial(n)))        