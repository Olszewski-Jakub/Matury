with open('liczby.txt') as liczby, open('pierwsze.txt') as pierwsze, open(
        'liczby_przyklad.txt') as liczby_przyklad, open('pierwsze_przyklad.txt') as pierwsze_przyklad:
    r = [liczby, pierwsze, liczby_przyklad, pierwsze_przyklad]
    dane = []
    for x in r:
        x = x.readlines()
        x = list(map(lambda x: int(x.rstrip()), x))
        dane.append(x)

    l, p = dane[0], dane[1]
    # l, p = dane[2], dane[3]


    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


    def a():
        for x in l:
            if is_prime(x) and 100 <= x <= 5000:
                print(x,end=" ")
        print()


    def b():
        for x in p:
            if is_prime(int(str(x)[::-1])):
                print(x, end=" ")
        print()


    def suma_cyfr(n):
        s = 0
        while n != 0:
            s += n % 10
            n //= 10
        return s

    def waga(n):
        while len(str(n)) != 1:
            n = suma_cyfr(n)
        return n
    def c():
        c = 0
        for x in p:
            c += waga(x) == 1
        print(c)

    a()
    b()
    c()