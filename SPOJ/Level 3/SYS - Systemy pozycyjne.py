def decToX(num, sys):
    s = ''
    while num != 0:
        r = num % sys
        num //= sys

        if r >= 10:
            s = chr(r + ord('A') - 10) + s
        else:
            s = str(r) + s

    return s


t = int(input())
for i in range(t):
    n = int(input())
    print(decToX(n, 16), end=" ")
    print(decToX(n, 11))
