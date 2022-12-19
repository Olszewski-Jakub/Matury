with open('przyklad.txt') as przyklad, open('instrukcje.txt') as instrukcje2:
    przyklad = przyklad.readlines()
    przyklad = list(map(lambda x: x.rstrip().split(), przyklad))
    instrukcje2 = instrukcje2.readlines()
    instrukcje2 = list(map(lambda x: x.rstrip().split(), instrukcje2))
    # print(instrukcje)

    # TODO zmienic liste
    dane = instrukcje2


    def a():
        z = [element[0] for element in dane]
        print(z.count('DOPISZ') - z.count("USUN"))


    def b():
        z = [element[0] for element in dane]
        funkcja, dl = z[0], 0
        m = 0
        m_d = ""
        for x in range(len(z)):
            if funkcja == z[x]:
                dl += 1
                if m < dl:
                    m = dl
                    m_d = funkcja
            else:
                funkcja = z[x]
                dl = 1

        print(m_d, m)


    def c():
        z = [x[1] for x in dane if x[0] == "DOPISZ"]
        sl = {}
        for x in z:
            if x not in sl.keys():
                sl[x] = 1
            else:
                sl[x] += 1
        print(max(sl, key=lambda x: sl[x]))


    # INSTRUKCJE
    def DOPISZ(r, ch):
        return r.append(ch)


    def ZMIEN(r, ch):
        r[len(r) - 1] = ch
        return r


    def USUN(r):
        r.pop(len(r) - 1)


    def next_alpha(s):
        return chr((ord(s.upper()) + 1 - 65) % 26 + 65)


    def PRZESUN(r, ch):
        for x in range(len(r)):
            if r[x] == ch:
                r[x] = next_alpha(ch)
                return r
        return r



    def d():
        instrukcje = [element[0] for element in dane]
        litery = [element[1] for element in dane]
        r = []
        for x in range(len(instrukcje)):
            print(instrukcje[x], litery[x])
            if instrukcje[x] == "DOPISZ":
                DOPISZ(r, litery[x])
            elif instrukcje[x] == "ZMIEN":
                ZMIEN(r, litery[x])
            elif instrukcje[x] == "USUN":
                USUN(r)
            else:
                PRZESUN(r, litery[x])
        print("".join(r))


    a()
    b()
    c()
    d()
