t = int(input())
t_c = 0


def te(c, x, y):
    if c % y == 0:
        return False
    return (c % x == 0)


while t_c < t:
    n, x, y = input().split()
    n = int(n)
    x = int(x)
    y = int(y)
    c = 0
    while c < n:
        if te(c, x, y):
            print(c, end=" ")
        c += 1
    print()
    t_c += 1
