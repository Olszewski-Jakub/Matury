from math import log10

with open('przyklad.txt') as przyklad, open('liczby.txt') as liczby:
    przyklad = przyklad.readlines()
    przyklad = list(map(lambda x: int(x.rstrip()), przyklad))
    liczby = liczby.readlines()
    liczby = list(map(lambda x: int(x.rstrip()), liczby))

    dane = liczby


    def isPowerOfThree(n):
        if not n or n < 0:
            return False
        return (log10(n) / log10(3)) % 1 == 0

    def factorial(k):
        a = 1
        for x in range(1,k+1):
            a *= x
        return a

    def a():
        c = 0
        for x in dane:
            if isPowerOfThree(x):
                c += 1
        print(c)

    def czy_iloczyn(n):
        r = [int(x) for x in str(n)]
        iloczyn = 0
        # print(n)
        for x in r:
            iloczyn += factorial(x)
            # print(iloczyn)
        # print()
        return iloczyn == n
    def b():
        for x in dane:
            if czy_iloczyn(x):
                print(x)

    def c():
        # Znajdź największy wspólny dzielnik każdej pary sąsiednich liczb
        gcd = []
        for i in range(len(dane) - 1):
            a = dane[i]
            b = dane[i + 1]
            while b != 0:
                a, b = b, a % b
            gcd.append(a)

        # Znajdź ciąg liczb, dla których największy wspólny dzielnik jest większy od 1 i jest najdłuższy ze wszystkich znalezionych ciągów
        longest_seq = []
        current_seq = []
        for i in range(len(gcd)):
            if gcd[i] > 1:
                current_seq.append(dane[i])
            else:
                if len(current_seq) > len(longest_seq):
                    longest_seq = current_seq
                current_seq = []

        # Podaj odpowiedź
        print("Pierwsza liczba w ciągu:", longest_seq[0])
        print("Długość ciągu:", len(longest_seq))
        print("Największy wspólny dzielnik wszystkich liczb w ciągu:", max(gcd))
    a()
    b()
    c()