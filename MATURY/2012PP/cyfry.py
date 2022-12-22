def suma_cyfr(n):
    s = 0
    while n != 0:
        s += n % 10
        n //= 10
    return s

def czy_ciag(n):
    r = []
    while n != 0:
        r.append(n % 10)
        n //= 10
    # print(r)
    for x in range(len(r)-1):
        if r[x] < r[x+1]:
            return False
        elif r[x] == r[x+1]:
            return False
    return True

with open('cyfry.txt') as cyfry:
    cyfry = cyfry.readlines()
    cyfry = list(map(lambda x: int(x.rstrip()), cyfry))
    # print(cyfry)

    # a)
    c = 0
    for x in cyfry:
        if x % 2 == 0:
            c += 1
    print(f"Jest {c} liczb parzystych")

    # b)
    r = []
    for x in cyfry:
        r.append(suma_cyfr(x))
    print(f"Najwieksza {cyfry[r.index(max(r))]} najmniejsza {cyfry[r.index(min(r))]}")

    # c)
    for x in cyfry:
        if czy_ciag(x):
            print(x)