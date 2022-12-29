while True:
    try:
        r = input().split()
        a, b, c = float(r[0]), float(r[1]), float(r[2])
        delta = b**2 - 4*a*c
        if delta < 0:
            print(0)
        elif delta == 0:
            print(1)
        else:
            print(2)
    except:
        break
