with open('liczby.txt') as liczby:
    liczby = list(map(lambda x: x.rstrip(), liczby.readlines()))


    def a():
        c = 0
        for x in liczby:
            if x.count('0') > x.count('1'):
                c += 1
        print(c)


    def b():
        c_2, c_8 = 0, 0
        for x in liczby:
            c_2 = c_2 + (1 if int(x, 2) % 2 == 0 else 0)
            c_8= c_8 + (1 if int(x, 2) % 8 == 0 else 0)

        print(c_2, c_8)

    def c():
        row_min, row_max = 0,0
        miniumum,maximum = float("inf"), 0
        for x in range(len(liczby)):
            if miniumum > int(liczby[x],2):
                row_min = x
                miniumum = int(liczby[x],2)
            if maximum < int(liczby[x],2):
                row_max = x
                maximum = int(liczby[x],2)
        print(row_min+1,row_max+1)
    a()
    b()
    c()
