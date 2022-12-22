def collatz(n , counter = 0):
    if n == 1:
        return counter
    elif n % 2 == 0:
        return collatz(n // 2, counter + 1)
    else:
        return collatz(3 * n + 1, counter + 1)

t = int(input())
while t>0:
    print(collatz(int(input())))

    t-=1