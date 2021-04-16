def func(a, b, c):
    x_1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
    x_2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
    result = print("해는 {} or {}".format(x_1, x_2))
    return result

func(1, 2, -8)

func(2, -6, -8)

func(2, -1, -6) #2x^2 -x -6