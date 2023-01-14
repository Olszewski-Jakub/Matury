with open('napisy.txt') as napisy:
    napisy = napisy.readlines()
    napisy = list(map(lambda x: x.rstrip().split(), napisy))


    # print(napisy)

    def a():
        c = 0
        r = []
        for x in napisy:
            if len(x[0]) >= 3 * len(x[1]) or len(x[1]) >= 3 * len(x[0]):
                if c == 0:
                    r = x
                c += 1
        print(c, *r)


    def b1(x):
        for y in range(len(x[0])):
            if x[0][y] != x[1][y]:
                return False
        return True


    def b():
        for x in napisy:
            if len(x[1]) > len(x[0]):
                if b1(x):
                    print(*x, x[1].replace(x[0], "", 1))


    def c1(x):
        test = True
        l1 = len(x[0]) - 1
        l2 = len(x[1]) - 1
        c = 0
        while test and l1 >= 0 and l2 >= 0:
            if x[0][l1] == x[1][l2]:
                c += 1
                l1 -= 1
                l2 -= 1
            else:
                return c
        return c


    def c():
        m = []
        for x in napisy:
            m.append(c1(x))
        print(max(m), m.count(max(m)))
        for x in napisy:
            if c1(x) == max(m):
                print(*x)



    a()
    b()
    c()