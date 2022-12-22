"""
Wejście
Najpierw liczba testów t (t ≤ 100). Następnie dla każdego testu liczba n (n ≤ 100) i n liczb oddzielonych spacjami.

Wyjście
Dla każdego testu n liczb w porządku odwrotnym niż na wejściu.
"""

n = int(input())
for x in range(n):
    print(*input().split(" ")[1:][::-1])
