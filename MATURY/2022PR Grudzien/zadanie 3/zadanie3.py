with open('liczby.txt') as liczby, open('liczby_przyklad.txt') as przyklad, open("wyniki3.txt", 'w') as wyniki:
    liczby = liczby.readlines()
    liczby = list(map(int, liczby))

    przyklad = przyklad.readlines()
    przyklad = list(map(int, przyklad))

    dane = liczby


    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


    def a():
        c = 0
        for x in dane:
            c += is_prime(x - 1)
        print(f"Zadanie 3.2 {c}",file=wyniki)


    def goldbach(n):
        results = []
        for i in range(2, n // 2 + 1):
            difference = n - i
            if is_prime(i) and is_prime(difference):
                results.append([i, difference])

        return results


    def b():
        unique_nums = set(dane)
        even_nums = filter(lambda x: x % 2 == 0, unique_nums)
        goldbach_results = map(
            lambda num: {"Liczba": num, "ilosc_rozkładow": len(goldbach(num))}, even_nums)

        sorted_goldbach_results = sorted(
            goldbach_results, key=lambda res: res['ilosc_rozkładow'])

        print(f"Zadanie 3.2",file=wyniki)
        print(f"najmniejsza {sorted_goldbach_results[0]}",file=wyniki)
        print(f"najwieksza: {sorted_goldbach_results[-1]}",file=wyniki)

    def c():
        slownik = {}
        for x in dane:
            for y in hex(x).replace("0x",""):
                if y in slownik:
                    slownik[y] += 1
                else:
                    slownik[y] = 1
        s = "0123456789abcdef"
        print("Zadanie 3.4",file=wyniki)
        for x in s:
            if x in slownik:
                print(f"{x.upper()}:{slownik[x]}",file=wyniki)
    # a()
    # b()
    c()