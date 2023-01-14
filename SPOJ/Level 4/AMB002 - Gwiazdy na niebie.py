from math import sqrt


def length(x, y):
    return sqrt(x * x + y * y)


t = int(input())
gwiazdy = []
for i in range(t):
    s = input().split()
    gwiazdy.append([s[0], length(int(s[1]), int(s[2]))])
