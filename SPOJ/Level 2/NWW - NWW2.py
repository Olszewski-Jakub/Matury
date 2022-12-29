# def najmniejsza_wspolna_wielokrotnosc(a):
#   M = max(a)
#   while True:
#     dzieli_wszystkie = True
#     for x in a:
#       if M % x != 0:
#         dzieli_wszystkie = False
#         break
#     if dzieli_wszystkie:
#       return M
#     M += 1
#
# t = int(input())
#
# for i in range(t):
#   n = int(input())
#   a = list(map(int, input().split()))
#   m = najmniejsza_wspolna_wielokrotnosc(a)
#   print(m)
from math import gcd

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        print(a[0])
        continue
    nww = a[0] * a[1] // gcd(a[0], a[1])
    for j in range(2, len(a)):
        nww = nww * a[j] // gcd(nww, a[j])
    print(nww)
