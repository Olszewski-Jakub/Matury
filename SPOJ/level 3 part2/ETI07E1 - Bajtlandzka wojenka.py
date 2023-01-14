karty = list(map(int, input().split()))
karty_przeciwnika = [x for x in range(1, 53) if x not in karty]

karty.sort()
c = 0
for x in karty:
    czy_wygrana = False
    for y in karty_przeciwnika:
        if x > y:
            c += 1
            karty_przeciwnika.remove(y)
            czy_wygrana = True
            break
    if not czy_wygrana:
        karty_przeciwnika.pop(len(karty_przeciwnika)-1)
print(c)