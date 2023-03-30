with open('szyfrogram.txt') as szyfrogram, open('czestosc.txt') as czestosc:
    szyfrogram = szyfrogram.readlines()
    szyfrogram = list(map(lambda x: x .rstrip(), szyfrogram))
    czestosc = czestosc.readlines()
    czestosc = list(map(lambda x: x.rstrip().split(), czestosc))
    print(czestosc)
    def a():
        slownik = {}
        for x in szyfrogram:
            for y in x:
                if y in slownik:
                    slownik[y] += 1
                else:
                    slownik[y] = 1
        for x in range(ord('A'), ord('Z')+1):
            if chr(x) in slownik.keys():
              print(chr(x), slownik[chr(x)])

    #7.2 odp Algorytm

    def c():
        result = ""
        for x in szyfrogram:
            for y in x:

                z =(ord(y) + int(czestosc[ord(y)-ord('A')][1]))
                if z > ord('Z'):
                    while ord('A') <= z <= ord('Z'):
                        z -= ord('A')
                # print(z)
                result += chr(z)
        print(result)


    a()
    c()




n = 26
t = [0] * n
with open("szyfrogram.txt", "r") as szyfr:
    for c in szyfr.read():
        if c.isupper():
            t[ord(c) - ord('A')] += 1

klucz = [''] * n
with open("czestosc.txt", "r") as czestosc:
    for line in czestosc:
        litera, ile = line.split()
        ile = int(ile)
        c = 'A'
        while t[ord(c) - ord('A')] != ile:
            c = chr(ord(c) + 1)
        klucz[ord(c) - ord('A')] = litera

with open("zadanie7_3.txt", "w") as zapis, open("szyfrogram.txt", "r") as szyfr:
    for s in szyfr:
        for i in range(len(s)):
            if s[i].isupper():
                zapis.write(klucz[ord(s[i]) - ord('A')])
        zapis.write('\n')