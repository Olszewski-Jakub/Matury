"""
Sprawdź, które spośród danych liczb są liczbami pierwszymi

Input
n - liczba testów n<100000, w kolejnych liniach n liczb z przedziału [1..10000]

Output
Dla każdej liczby słowo TAK, jeśli liczba ta jest pierwsza, słowo: NIE, w przeciwnym wypadku.
"""


def is_prime(k):
    if k < 2:
        return False
    for i in range(2, k):
        if k % i == 0:
            return False
    return True


n = int(input())
for x in range(n):
    k = int(input())
    print("TAK" if is_prime(k) else "NIE")
