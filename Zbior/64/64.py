with open('dane_obrazki.txt') as obrazki:
    def print_obrazek(a):
        for x in a[:-1]:
            print(x[:-1])
        print()


    # print(obrazki.readlines())
    obrazki = obrazki.readlines()
    obrazki = list(map(lambda x: x.rstrip(), obrazki))
    r = []
    for x in range(200):
        temp = []
        for y in range(21):
            temp.append(obrazki[22 * x + y])
        r.append(temp)


    # for x in r:
    #     print_obrazek(x)

    def a():
        count = 0
        max_1 = 0
        for x in r:
            count_0, count_1 = 0, 0
            for y in x[:-1]:
                y = y[:-1]
                count_0 += y.count('0')
                count_1 += y.count('1')
            max_1 = max(max_1, count_1)
            if count_1 > count_0:
                count += 1

        print(count, max_1)


    def b1(r):
        for x in range(10):
            for y in range(10):
                temp = set([r[x][y], r[x + 10][y], r[x][y + 10], r[x + 10][y + 10]])
                if len(temp) != 1:
                    return False
        return True


    def b():
        count = 0
        for x in r:
            if b1(x):
                if count == 0:
                    print_obrazek(x)
                count += 1
        print(count)


    def c():
        poprawne,naprawialne,niepoprawne = 0,0,0
        for x in r:
            error_x = 0
            error_y = 0
            # Ddla OX
            for y in x[:-1]:
                if y[:-1].count('1') % 2 != int(y[20]):
                    error_x += 1
            # Dla OY
            for a in range(20):
                count = 0
                for b in range(20):
                    if x[b][a] == '1':
                        count += 1
                if count % 2 != int(x[20][a]):
                    error_y += 1

            if error_x == error_y == 0:
                poprawne+=1
            elif error_x <= 1 and error_y <= 1:
                naprawialne +=1
            else:
                niepoprawne +=1

        print(poprawne,naprawialne,niepoprawne)
    # a()

    # b()
    c()