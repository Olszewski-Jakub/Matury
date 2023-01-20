with open('liczby1.txt') as liczby1, open('liczby2.txt') as liczby2, open('liczby3.txt') as liczby3:
    liczby1 = liczby1.readlines()
    liczby1 = list(map(lambda x: int(x.rstrip(),2),liczby1))
    liczby2 = liczby2.readlines()
    liczby2 = list(map(lambda x: int(x.rstrip(), 2), liczby2))
    liczby3 = liczby3.readlines()
    liczby3 = list(map(lambda x: int(x.rstrip(), 2), liczby3))
    print(liczby1)
    print(liczby2)
    print(liczby3)

    l1_2,l1_3,l1_5 = 0,0,0
    for x in liczby1:
        l1_2 += x%2==0
        l1_3 += x%3==0
        l1_5 += x%4==0
    print(f"2: {l1_2}")
    print(f"3: {l1_3}")
    print(f"5: {l1_5}")

    print()
    l2_2, l2_3, l2_5, =0,0,0
    for x in liczby2:
        l2_2 += x%2 == 0
        l2_3 += x%3 == 0
        l2_5 += x%5 == 0
    print(f"2: {l2_2}")
    print(f"3: {l2_3}")
    print(f"5: {l2_5}")

    print()
    l3_2, l3_3, l3_5, = 0, 0, 0
    for x in liczby3:
        l3_2 += x % 2 == 0
        l3_3 += x % 3 == 0
        l3_5 += x % 5 == 0
    print(f"2: {l3_2}")
    print(f"3: {l3_3}")
    print(f"5: {l3_5}")