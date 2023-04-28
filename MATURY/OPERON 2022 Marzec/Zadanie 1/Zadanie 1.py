with open('liczby.txt') as liczby:
    liczby = liczby.readlines()
    liczby = list(map(lambda x: x.rstrip(), liczby))


    # print(liczby)

    def a():
        count = 0
        for x in liczby:
            for y in liczby:
                if x == y[::-1] and x != y:
                    count += 1
        print(count)


    def isPrime(n):
        if n < 2:
            return False
        for x in range(2, int(n ** 0.5) + 1):
            if n % x == 0:
                return False
        return True


    def b():
        pary = []
        wystepuje = []
        for x in liczby:
            if len(x) >= 2:
                lustrzana = x[::-1]
                if isPrime(int(x)) and isPrime(int(lustrzana)) and int(x) not in wystepuje and int(
                        lustrzana) not in wystepuje:
                    pary.append([int(x), int(lustrzana)])
                    wystepuje.append(int(x))
        pary.sort(key=lambda z: min(z))
        for x in pary:
            print(*x)
        print(len(pary))


    from math import gcd

    def c():
        dane = []
        for x in liczby:
            if len(x) >= 2:
                lustrzana = x[::-1]
                liczba = int(x + str((lustrzana)))
                dane.append(liczba)
        print(dane)
        nwd  = gcd(dane[0],dane[1])
        print(nwd)
        for x in dane[2::]:
            nwd = gcd(nwd, x)
        print(nwd)


    def is_triangular_number(n):
        i = 1
        while n > 0:
            n -= i
            i += 1
        return n == 0



    def d():
        count = 0
        for x in liczby:
            if len(x) >=2:
                liczba = int(x)
                lustrzana = int(x[::-1])
                count += is_triangular_number(liczba+lustrzana)
        print(count)
    d()
    # a()
    # b()
    # c()
