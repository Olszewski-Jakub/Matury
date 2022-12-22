with open('dane_napisy.txt') as dane:
    dane = dane.readlines()
    dane = list(map(lambda x: x.rstrip().split(), dane))


    def litery(r):
        s1, s2 = {}, {}
        r1, r2 = r[0], r[1]
        for x in r1:
            if x not in s1:
                s1[x] = 1
            else:
                s1[x] += 1
        for y in r2:
            if y not in s2:
                s2[y] = 1
            else:
                s2[y] += 1

        return [s1, s2]


    def a():
        c= 0
        for x in dane:
            s1,s2 = litery(x)
            if len(s1) == 1 and len(s2) == 1 and s1 == s2:
                c+=1
        print(c)

    def b():
        c = 0
        for x in dane:
            s1,s2 = litery(x)
            if s1 == s2:
                c+=1
        print(c)

    def c():
        lista_liter = []
        for x in dane:
            s1,s2 = litery(x)
            lista_liter.append(s1)
            lista_liter.append(s2)
        m = 0
        for x in lista_liter:
            c = 0
            for y in lista_liter:
                if x==y:
                    c+=1
            m = max(m,c)
        print(m)
    c()