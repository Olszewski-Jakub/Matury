while True:
    try:
        r = [x for x in input()]
        for x in range(len(r) - len(r) % 2,2):
            r[x], r[x + 1] = r[x + 1], r[x]

        print("".join(r))
    except:
        break
