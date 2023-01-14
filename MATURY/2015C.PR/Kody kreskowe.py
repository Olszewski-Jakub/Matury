with open('kody.txt') as kody, open('kody1.txt', 'w') as kody1:
    kody = kody.readlines()
    kody = list(map(lambda x: x.rstrip(), kody))


    def a():
        for x in kody:
            parzyste = int(x[5]) + int(x[3]) + int(x[1])
            nieparzyste = int(x[4]) + int(x[2]) + int(x[0])
            print(parzyste, nieparzyste, file=kody1)


    def b():
        for x in kody:
            parzyste = int(x[5]) + int(x[3]) + int(x[1])
            nieparzyste = int(x[4]) + int(x[2]) + int(x[0])
            kontrolna = (10 - (3 * parzyste + nieparzyste) % 10) % 10

            slownik = {
                "0": "10101110111010",
                "1": "11101010101110",
                "2": "10111010101110",
                "3": "11101110101010",
                "4": "10101110101110",
                "5": "11101011101010",
                "6": "10111011101010",
                "7": "10101011101110",
                "8": "11101010111010",
                "9": "10111010111010"
            }

            print(kontrolna, slownik[str(kontrolna)])


    def encode_code25(number):
        # tabela kodów cyfr
        codes = {
            '0': '10101110111010',
            '1': '11101010101110',
            '2': '10111010101110',
            '3': '11101110101010',
            '4': '10101110101110',
            '5': '11101011101010',
            '6': '10111011101010',
            '7': '10101011101110',
            '8': '11101010111010',
            '9': '10111010111010'
        }

        # znak start
        encoded = '11011010'

        # kodowanie cyfr liczby
        for digit in str(number):
            encoded += codes[digit]

        # obliczanie cyfry kontrolnej
        even_sum = sum(int(digit) for i, digit in enumerate(str(number)) if i % 2 == 0)
        odd_sum = sum(int(digit) for i, digit in enumerate(str(number)) if i % 2 != 0)
        control_digit = (even_sum * 3 + odd_sum) % 10
        if control_digit != 0:
            control_digit = 10 - control_digit
        encoded += codes[str(control_digit)]

        # znak stop
        encoded += '11010110'

        return encoded
    def c():
        for x in kody:
            print(encode_code25(x))


    a()
    b()
    c()
