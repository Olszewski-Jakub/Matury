with open('dane.txt') as dane1, open('dane_przyklad.txt') as przyklad:
    # dane = dane1
    dane = przyklad
    dane = dane.readlines()
    dane = list(map(lambda x: int(x.rstrip()), dane))


    # print(dane)

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


    def a():
        max_num, min_num, count = 0, 100000000000000, 0
        for x in dane:
            if is_prime(x):
                count += 1
                max_num = max(x, max_num)
                min_num = min(x, min_num)
        print(count, max_num, min_num)


    def is_palindrome_or_almost(n):
        binary = bin(n)[2:]
        length = len(binary)
        for i in range(length // 2):
            if binary[i] != binary[length - i - 1]:
                if i == length // 2 - 1 and binary[i + 1] == "0":
                    return True
                return False
        return True


    def b():
        count = 0
        for x in dane:
            if is_prime(x):
                count += 1
        print(count)


    def c():
        pairs = set()
        z = list(map(str, dane))
        for i in range(len(z)):
            for j in range(i + 1, len(z)):
                if set(z[i]) == set(z[j]):
                    pairs.add((z[i], z[j]))
        print(len(pairs))


    a()
    b()
    c()
