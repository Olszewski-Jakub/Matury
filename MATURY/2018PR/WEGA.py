with open('sygnaly.txt') as sygnaly, open('przyklad.txt') as przyklad:
    sygnaly = sygnaly.readlines()
    sygnaly = list(map(lambda x: x.rstrip(), sygnaly))
    przyklad = przyklad.readlines()
    przyklad = list(map(lambda x: x.rstrip(), przyklad))

    dane = sygnaly


    def litery(s):
        slownik = {}
        for x in s:
            if x not in slownik:
                slownik[x] = 1
            else:
                slownik[x] += 1

        return len(slownik)


    def a():
        s = ""
        for x in range(39, len(dane), 40):
            s += dane[x][9]
        print(s)


    def znajdz_slowa(slowa,dl_slowa):
        r = []
        for x in slowa:
         if x[1] == dl_slowa:
             r.append(x)
        return r

    def b():
        slowa = []
        for x in dane:
            slowa.append([x, litery(x)])

        dl_slow = max([x[1] for x in slowa])
        x = znajdz_slowa(slowa,dl_slow)
        print(x[0][0] if len(x) == 1 else x[0:1][0])

    def oldeglosc(s):
        for x in range(len(s)-1):
            if abs(ord(s[x])-ord(s[x+1])) > 10:
                return False
        return True

    def c():
        for x in dane:
            if oldeglosc(x):
                print(x)
    a()
    b()
    c()