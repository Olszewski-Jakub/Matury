with open('przyklad.txt') as przyklad, open('pary.txt') as pary:
    przyklad = przyklad.readlines()
    przyklad = list(map(lambda x: x.rstrip().split(), przyklad))
    pary = pary.readlines()
    pary = list(map(lambda x: x.rstrip().split(), pary))

    dane = pary
    print(dane)




    # Funkcja sprawdzająca, czy liczba jest pierwsza
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


    def a():
        even_numbers = [int(x[0]) for x in dane if int(x[0])%2==0]
        for n in even_numbers:
            max_diff = 0
            p1 = 0
            p2 = 0
            for i in range(2, n):
                if is_prime(i):
                    for j in range(2, n):
                        if is_prime(j) and i + j == n:
                            if abs(i - j) > max_diff:
                                p1 = i
                                p2 = j
                                max_diff = abs(i - j)
            print(f"{n} = {min(p1, p2)} + {max(p1, p2)}")

    def b():
        words = [x[1] for x in dane]
        for word in words:
            max_len = 0
            max_substr = ''
            for i in range(len(word)):
                for j in range(i + 1, len(word) + 1):
                    substr = word[i:j]
                    if len(substr) > max_len and all(c == substr[0] for c in substr):
                        max_len = len(substr)
                        max_substr = substr
            print(f"{max_substr} {max_len}")


    def count_unique_letters(string):
        unique_letters = set()
        for letter in string:
            unique_letters.add(letter)
        return len(unique_letters)

    def c():
        r = []
        for x in dane:
            if int(x[0]) == len(x[1]):
                r.append(x)
        min = []
        for x in r:
            for y in r:
                if int(x[0]) < int(y[0]):
                    min = x
                if int(x[0]) == int(y[0]) and count_unique_letters(x[1])<count_unique_letters(y[1]):
                    min = x
        print(min)
    # a()
    # b()
    c()