from math import sqrt

with open('trojki.txt') as trojki, open("wyniki_trojki.txt", 'w') as wyniki:
    trojki = trojki.readlines()
    trojki = list(map(lambda x: list(map(lambda y: int(y), x.rstrip().split())), trojki))


    # print(trojki)

    def is_prime(n):
        for i in range(2, int(sqrt(n)) + 1):
            if (n % i) == 0:
                return False
        return True


    def ab(a, b):
        if not is_prime(a):
            return False
        if not is_prime(b):
            return False
        return True


    def suma_cyfr(n):
        s = 0
        while n != 0:
            s += n % 10
            n //= 10
        return s


    def isRight(r):
        r.sort()
        return r[0] ** 2 + r[1] ** 2 == r[2] ** 2


    def isTriangle(r):
        return r[0] + r[1] > r[2]


    def a():
        print('Zadanie 1.3', file=wyniki)
        for x in trojki:
            if suma_cyfr(x[0]) + suma_cyfr(x[1]) == x[2]:
                print(*x, file=wyniki)


    def b():
        print('\nZadanie 2', file=wyniki)

        for x in trojki:
            if ab(x[0], x[1]) and x[2] == x[0] * x[1]:
                print(*x, file=wyniki)


    def c():
        print('\nZadanie 3', file=wyniki)

        for x in range(len(trojki) - 1):
            if isRight(trojki[x]) and isRight(trojki[x + 1]):
                print(*trojki[x], file=wyniki)
                print(*trojki[x + 1], '\n', file=wyniki)


    def d():
        print('\nZadanie 4', file=wyniki)
        count = 0
        sequnce = 1
        sequnce_max = 0
        for x in range(len(trojki)):
            trojki[x].sort()
            if isTriangle(trojki[x]):
                count += 1

        for x in range(len(trojki)-1):
            if isTriangle(trojki[x]) and isTriangle(trojki[x+1]):
                sequnce += 1
            else:
                if sequnce_max < sequnce:
                    sequnce_max = sequnce
                sequnce = 0
        print(count, file=wyniki)
        print(sequnce_max, file=wyniki)

    a()
    b()
    c()
    d()
