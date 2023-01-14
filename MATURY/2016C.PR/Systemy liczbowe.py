with open('liczby.txt') as liczby:
    liczby = liczby.readlines()
    liczby = list(map(lambda x: (x.rstrip()), liczby))


    # print(liczby)

    def a():
        c = 0
        for x in liczby:
            c += x[-1] == "8"
        print(c)


    def b():
        c = 0
        for x in liczby:
            c += x[-1] == "4" and x.count("0") == 0
        print(c)


    def c():
        c = 0
        for x in liczby:
            c += x[-1] == "2" and int(x[0:len(x) - 1], 2) % 2 == 0
        print(c)


    def d():
        sum = 0
        for x in liczby:
            if x[-1] == "8":
                sum += int(x[0:len(x) - 1], 8)
        print(sum)


    def e1():
        r = []
        for x in liczby:
            r.append(int(x[0:len(x) - 1], int(x[-1])))
        return max(r), min(r)


    def e():
        najw,najm = False,False
        najwieksza, najmniejsza = e1()
        for x in liczby:
            if int(x[0:len(x) - 1], int(x[-1])) == najwieksza and not najw:
                print(f"Najwieksza {x}, {najwieksza}")
                najw = True

            if int(x[0:len(x) - 1], int(x[-1])) == najmniejsza and not najm:
                print(f"najmniejsza {x}, {najmniejsza}")
                najm = True

a()
b()
c()
d()
e()