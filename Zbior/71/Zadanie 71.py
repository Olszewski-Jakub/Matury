with open('funkcja.txt') as funkcja:
    funkcja = funkcja.readlines()
    funkcja = list(map(lambda x: list(map(float, x.rstrip().split())), funkcja))


    # x0 + x1*x + x2*x^2 + x3*x^3
    def f(x):
        if x < 1.0:
            return ((funkcja[0][3] * x + funkcja[0][2]) * x + funkcja[0][1]) * x + funkcja[0][0]
        elif x < 2.0:
            return ((funkcja[1][3] * x + funkcja[1][2]) * x + funkcja[1][1]) * x + funkcja[1][0]
        elif x < 3.0:
            return ((funkcja[2][3] * x + funkcja[2][2]) * x + funkcja[2][1]) * x + funkcja[2][0]
        elif x < 4.0:
            return ((funkcja[3][3] * x + funkcja[3][2]) * x + funkcja[3][1]) * x + funkcja[3][0]
        else:
            return ((funkcja[4][3] * x + funkcja[4][2]) * x + funkcja[4][1]) * x + funkcja[4][0]


    def a(arg):
        print(round(f(arg), 5))


    def b():
        mx, mfx = 0, 0
        for x in range(0, 500001):
            x = x / 100000
            fx = f(x)
            if fx > mfx:
                mx, mfx = x, fx
        print(str(round(mx, 3))), str(round(mfx, 5))
        a(mx)


    def bisekcja(left, right):
        fl = f(left)
        while right - left > 1e-8:
            middle = (left + right) / 2.0
            fm = f(middle)
            if fl * fm < 0.0:
                right = middle
            else:
                left = middle
                fl = fm
        return round((left + right) / 2.0, 5)


    def c():
        for x in range(0, 5):
            if f(x) * f(x + 1) < 0:
                root = bisekcja(x, x + 1)
                print((root))

    a(1.5)
    b()
    c()
