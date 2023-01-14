from string import ascii_uppercase

with open('tekst.txt') as napisy:
    napisy = napisy.readline().rstrip()
    napisy1 = napisy.replace(" ", "")
    napisy = napisy.split()


    # print(len(napisy))

    def a():
        c = 0
        for x in napisy:
            for y in range(len(x) - 1):
                if x[y] == x[y + 1]:
                    c += 1
                    break
        print(c)


    def b():
        # print(len(napisy1))
        lista = {}
        for x in napisy1:
            if x in lista:
                lista[x] += 1
            else:
                lista[x] = 1

        for x in sorted(lista.keys()):
            print(f"{x} : {lista[x]} ({lista[x] / sum(lista.values()) * 100:.2f}%)")


    def c1(x):
        r = "AEIOUY"

        temp = x[0]
        c = 0
        z = []
        for y in range(len(x)):
            if temp not in r and x[y] not in r:
                c += 1
            elif len(x) - 1 == y and c != 1:
                z.append(c)
            else:
                z.append(c)
                c = 1
            temp = x[y]
        return max(z)


    def c2(s):
        r = "AEIOUY"
        for x in s:
            if x in r:
                return False
        return True


    def c():
        m = 0
        rr = []
        for x in napisy:
            c = c1(x)
            m = max(m, c)
            rr.append(c)
        print(rr)
        for x in napisy:
            if c1(x) == max(rr):
                print(x)
                break

        print(m, rr.count(m))


    a()
    b()
    c()
