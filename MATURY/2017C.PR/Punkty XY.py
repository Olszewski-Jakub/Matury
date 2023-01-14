from math import sqrt

with open('punkty.txt') as punkty:
    punkty = punkty.readlines()
    punkty = list(map(lambda x: list(map(int, x.rstrip().split())), punkty))


    # print(punkty)

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


    def a():
        c = 0
        for x, y in punkty:
            c += is_prime(x) and is_prime(y)
        print(c)


    def b1(n):
        n = str(n)
        s = []
        for x in n:
            s.append(x)
        return set(s)


    def b():
        c = 0
        for x, y in punkty:
            s1, s2 = b1(x), b1(y)
            c += s1 == s2
        print(c)


    def odleglosc(x1, y1, x2, y2):
        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


    def c():
        zestaw = []
        najbarzfeij = 0
        for x1, y1 in punkty:
            for x2, y2 in punkty:
                odl = odleglosc(x1, y1, x2, y2)
                if najbarzfeij < odl:
                    najbarzfeij = odl
                    zestaw = [[x1, y1], [x2, y2]]
        print(round(najbarzfeij), zestaw)


    def d():
        x_max = 5000
        x_min = -5000
        y_max = 5000
        y_min = -5000
        wewnatrz, na_bokach, nazewnatrz = 0, 0, 0
        for x, y in punkty:
            wewnatrz += x_min < x < x_max and y_min < y < y_max
            nazewnatrz += x < x_min or x > x_max or y < y_min or y > y_max
            na_bokach = len(punkty) - wewnatrz - nazewnatrz
        print(wewnatrz, na_bokach, nazewnatrz)


    a()
    b()
    c()
    d()
