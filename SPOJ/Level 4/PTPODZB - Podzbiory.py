def podzbior(tablica, index, elements, elementy=[]):
    if len(elementy) == elements:
        print(*elementy)
    elif index < len(tablica):
        podzbior(tablica, index + 1, elements, elementy + [tablica[index]])
        podzbior(tablica, index + 1, elements, elementy)


t = int(input())
for i in range(t):
    n, k = input().split()
    r = [x for x in range(1, int(n) + 1)]
    podzbior(r, 0, int(k))
    print()