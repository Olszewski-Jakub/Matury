def ciekawa_liczba(k):
    ciekawe_liczby = ["5", "6"]
    if k < 3:
        return ciekawe_liczby[k-1]
    for i in range(2, k):
        ciekawe_liczby_tmp = []
        for liczba in ciekawe_liczby:
            ciekawe_liczby_tmp.append(liczba+"5")
            ciekawe_liczby_tmp.append(liczba+"6")
        ciekawe_liczby = ciekawe_liczby_tmp
    return ciekawe_liczby[k-1]

k = 10
print(ciekawa_liczba(k))
