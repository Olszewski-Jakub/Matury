with open('dane6.txt') as dane, open('dane6przyklad.txt') as przyklad:
    liczby = dane
    # liczby = przyklad
    liczby = liczby.readlines()
    liczby = list(map(lambda x: x.rstrip(), liczby))
    print(liczby)


    def a():
        wynik = [0] * 9
        for x in range(2, 11):
            for y in liczby:
                if str(x-1) in y and max([int(z) for z in y]) <= x-1:
                    wynik[x-2] += 1
        print(wynik)

    def b():
        wynik = [''] * 9
        for x in range(2, 11):
            liczba_max = ""
            suma_max = 0
            for y in liczby:
                if str(x - 1) in y and max([int(z) for z in y]) <= x - 1:
                    temp = sum([int(a) for a in y])
                    if temp > suma_max:
                        liczba_max = y
                        suma_max = temp
            wynik[x-2] = liczba_max
        for x in range(2,11):
            print(x, wynik[x-2])


    def c1(x):
        if len(x) == 1:
            return True
        for n in range(len(x)):
            for i in range(len(x)):
                if x[i] == x[len(x)-i-1]:
                    return False
        return True
    def c():
        for x in liczby:
            if c1(x):
                print(x)


    a()
    b()
    c()