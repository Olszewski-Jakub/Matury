def rysuj(x, y, strzaly):
    if 2 * x <= N:
        if 2 * x == y:
            strzaly.append((x, y))
        else:
            rysuj(2 * x, y, strzaly)
    if 2 * x + 1 <= N:
        if 2 * x + 1 == y:
            strzaly.append((x, y))
        else:
            rysuj(2 * x + 1, y, strzaly)


N = 100000
strzaly = []

with open('pary.txt', 'r') as f, open('wyniki2.txt', 'w') as wyniki:
    for line in f:
        x, y = map(int, line.split())
        rysuj(x, y, strzaly)

    for x, y in strzaly:
        print(f'{x} {y}', file=wyniki)
