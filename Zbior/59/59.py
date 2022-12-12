def sieve(n):
    r = [1] * (n + 1)
    r[0] = r[1] = 0
    p = 2
    while p * p <= n:
        if r[p] == 1:
            for i in range(2 * p, n + 1, p):
                r[i] = 0
        p += 1

    return r


def na_czynniki(n):
    if n % 2 == 0:
        return False
    r = []
    naczynnik = 3
    while n != 1:
        if len(set(r)) > 3:
            return False
        if n % naczynnik == 0:
            r.append(n)
            n //= naczynnik
        else:
            naczynnik += 2

    return len(set(r)) == 3


def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p * 2, n + 1, p)))
    return primes


def b(n):
    x = n + int(str(n)[::-1])
    return x == x[::-1]

with open('liczby.txt') as liczby, open("odp.txt", 'w') as odp:
    liczby = liczby.readlines()
    liczby = list(map(lambda x: int(x.rstrip()), liczby))

    # print(liczby)
    # s = sieve(max(liczby))
    # primes = []
    # for x in range(2,len(s)):
    #     if s[x] == 1:
    #         primes.append(x)
    # print(primes)

    # print(get_primes(max(liczby)))
    c=0
    for x in liczby:
        if na_czynniki(x):
            c+=1
            print(x)