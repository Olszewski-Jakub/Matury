# odczytanie napisów i klucza z pliku
with open("szyfr1.txt", "r") as file:
    lines = file.readlines()
    plaintexts = lines[:6]
    plaintexts = list(map(lambda x: x.rstrip(), plaintexts))
    key = list(map(int, lines[6].split()))

    for x in plaintexts:
        r = [" "] * len(x)
        for y in range(len(x)):
            temp = x[y]
            r[y] =x[key[y]-1]
            r[key[y]-1] = temp

        print("".join(r))


n = 15
P = [0] * n

with open("szyfr2.txt", "r") as f:
    def szyfr(A):
        for i in range(len(A)):
            A[i], A[P[i % n] - 1] = A[P[i % n] - 1], A[i]
        return "".join(A)
    tekst = f.readline()
    P = [int(x) for x in f.readline().split()]
    print(szyfr(list(tekst)))


with open('szyfr3.txt') as tekst:
    tekst = tekst.readlines()[0].rstrip()
    n = 6
    P = [6, 2, 4, 1, 5, 3]

    def deszyfr(A):
        for i in range(len(A)-1, -1, -1):
            A[i], A[P[i%n]-1] = A[P[i%n]-1], A[i]
        return "".join(A)


    print(deszyfr(list(tekst)))
