def maks(a, b, c):
    return sorted([a, b, c])


def rodzaj(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        a, b, c = maks(a, b, c)
        if a * a + b * b == c * c:
            print("prostokatny")
        elif a * a + b * b > c * c:
            print("ostrokatny")
        else:
            print("rozwartokatny")
    else:
        print("brak")



while True:
    try:
        a, b, c = map(int, input().split())
        rodzaj(a, b, c)
    except:
        break
