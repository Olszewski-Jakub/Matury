def fkcja(liczba):
    if liczba < 10:
        print(liczba)
    else:
        fkcja(liczba // 10)
        print(liczba % 10)


fkcja(1234)

def minus_binary_to_decimal(minus_binary):
    decimal = 0
    power = 0
    for i in range(len(minus_binary)):
        if minus_binary[i] == '1':
            decimal -= pow(-2, power)
        power += 1
    return decimal

print(minus_binary_to_decimal('000111'))