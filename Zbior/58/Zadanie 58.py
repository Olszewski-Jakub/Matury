from math import ceil

with open('dane_systemy1.txt') as s1, open('dane_systemy2.txt') as s2, open('dane_systemy3.txt') as s3:
    # 1 - bin
    # 2- 4
    # 3- 8
    s1 = s1.readlines()
    s1 = list(map(lambda x: list(map(lambda y: int(y, 2), x.rstrip().split())), s1))
    s2 = s2.readlines()
    s2 = list(map(lambda x: list(map(lambda y: int(y, 4), x.rstrip().split())), s2))
    s3 = s3.readlines()
    s3 = list(map(lambda x: list(map(lambda y: int(y, 8), x.rstrip().split())), s3))

    # 58.1
    min1, min2, min3 = float('inf'), float('inf'), float('inf')
    for x in s1:
        if x[1] < min1:
            min1 = x[1]
    print(f"Stacja 1: {bin(min1).replace('0b', '')}")
    for x in s2:
        if x[1] < min2:
            min2 = x[1]
    print(f"Stacja 2: {bin(min2).replace('0b', '')}")
    for x in s3:
        if x[1] < min3:
            min3 = x[1]
    print(f"Stacja 3: {bin(min3).replace('0b', '')}")

    # 58.2
    c = 0
    h1, h2, h3 = s1[0][0], s2[0][0], s3[0][0],
    for x in range(len(s1) - 1):
        if h1 != s1[x][0] and h2 != s2[x][0] and h3 != s3[x][0]:
            c += 1
        h1 += 24
        h2 += 24
        h3 += 24
    print(f"Liczba dni z blednymi rekordami {c}")

    # 58.3
    r1, r2, r3 = [s1[0][1]], [s2[0][1]], [s3[0][1]]
    rekord = 1
    for x in range(1, len(s1)):
        if max(r1) < s1[x][1] or max(r2) < s2[x][1] or max(r3) < s3[x][1]:
            rekord += 1
        r1.append(s1[x][1])
        r2.append(s2[x][1])
        r3.append(s3[x][1])
    print(f"Liczba rekordow to {rekord}")

    # 58.4
    skok_max = 0
    for i in range(len(s1)):
        for j in range(len(s1)):
            r_ij = (s1[i][1] - s1[j][1]) ** 2
            ij_abs = abs(i-j)
            skok = ceil(r_ij / ij_abs) if ij_abs != 0 else 0
            if skok_max < skok: skok_max = skok
    print(skok_max)