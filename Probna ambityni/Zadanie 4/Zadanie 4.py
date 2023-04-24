with open('pasy.txt') as dane, open('wynik4.txt', 'w') as wynik:
    dane = dane.readlines()
    dane = list(map(lambda x: x.rstrip(), dane))
    # print(dane)
    lotniska = []
    temp = []
    for x in dane:
        if len(x) > 0:
            temp.append(x.split())

        else:
            # print(temp)
            lotniska.append(temp)
            temp = []


    # print(lotniska)
    def f7(lista):
        seen = set()
        seen_add = seen.add
        return [x for x in lista if not (x in seen or seen_add(x))]


    def a():
        r = []
        for x in lotniska:
            for y in x:
                for z in x:
                    if y[2] == z[2]:
                        if y[2] == '360':
                            if int(y[0]) < int(z[0]):
                                r.append([*z, 'R'])
                                r.append([*y, 'L'])
                            else:
                                r.append([*y, 'R'])
                                r.append([*z, 'L'])
                        elif y[2] == '180':
                            if int(y[0]) > int(z[0]):
                                r.append([*z, 'R'])
                                r.append([*y, 'L'])
                            else:
                                r.append([*y, 'R'])
                                r.append([*z, 'L'])
                        elif y[2] == '90':
                            if int(y[1]) > int(z[1]):
                                r.append([*z, 'R'])
                                r.append([*y, 'L'])
                            else:
                                r.append([*y, 'R'])
                                r.append([*z, 'L'])
                        elif y[2] == '270':
                            if int(y[1]) < int(z[1]):
                                r.append([*z, 'R'])
                                r.append([*y, 'L'])
                            else:
                                r.append([*y, 'R'])
                                r.append([*z, 'L'])
        r2 = []
        for x in r:
            r2.append(" ".join(x))
        result = f7(r2)
        print("ZAdanie 4.2", file=wynik)
        for x in result:
            print(x, file=wynik)


    def b():
        count = 0
        for x in lotniska:
            temp = 0
            for y in x:
                for z in x:
                    if y[2] == '360' and (z[2] == '90' or z[2] == '270'):
                        temp += 1
                    if y[2] == '180' and (z[2] == '90' or z[2] == '270'):
                        temp += 1
            if temp > 0:
                count += 1
        print(f"Zadanie 4.3\n{count}", file=wynik)


    def c():
        r = []
        for x in lotniska:
            temp = []
            for y in x:
                a = y[0]
                b = y[1]
                c = y[2]
                if c == '90':
                    c = '270'
                if c == '180':
                    c = '360'
                temp.append(a+b+c)
            r.append(len(set(temp)))
        print(f"ZAdanie 4.4\nMax {max(r)}\nMin {min(r)}",file=wynik)


    a()
    b()
    c()
