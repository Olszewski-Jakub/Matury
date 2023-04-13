# 3.1
"""
5
2
6
1
"""

# 3.2
"""

funkcja potęga(a, x, M)
    jeżeli x = 0
        b <- 1
    jeżeli x mod 2 == 0:
        w <- potęga(a, x/2)
        b <- w*w mod M
    jeżeli x mod 2 == 1:
        w <- potęga(a, (x-1)/2)
        zwróć b <- a*w*w mod M

"""
import math
import threading


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    return True


def nwd(a, b): return nwd(b, a % b) if b else a
from math import gcd
# NWD
with open('liczby.txt') as liczby, open('liczby_przyklad.txt') as przyklad:
    dane = liczby
    # dane = przyklad

    dane = dane.readlines()
    dane = list(map(lambda x:
                    list(map(int, x.rstrip().split()))
                    , dane))


    # print(dane)

    def a():
        count = 0
        for x in dane:
            count += is_prime(x[0])
        print(count)


    def b():
        count = 0
        for x in dane:
            count += nwd(x[0], x[1]) == 1

        print(count)


    def c1(M, a, b):
        for x in range(M):
            if a ** x % M == b:
                return True
        return False


    def c():
        count = 0
        for trojki in dane:
            count += c1(trojki[0], trojki[1], trojki[2])
        print(count)


    a()
    b()
    c()

    """
    odpowiedzi 
    343
    712
    764
    """
