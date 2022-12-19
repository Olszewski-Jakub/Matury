with open('dane_6_1.txt') as dane1, open('dane_6_2.txt') as dane2, open('dane_6_3.txt') as dane3:
    dane1 = list(map(lambda x: x.rstrip(),dane1.readlines()))
    dane2 = list(map(lambda x: x.rstrip().split(),dane2.readlines()))
    dane3 = list(map(lambda x: x.rstrip().split(),dane3.readlines()))


    def ceasar_cipher(word, k):
        result = ''
        for c in word:
            result += chr((ord(c) - ord('A') + k) % 26 + ord('A'))
        return result


    def ceasar_decipher(cipher, k):
        result = ''
        for c in cipher:
            result += chr((ord(c) - ord('A') - k) % 26 + ord('A'))
        return result

    def a():
        for x in dane1:
            print(ceasar_cipher(x,107))


    def b():
        for x in dane2:
            if len(x) == 1:
                x.append(0)
            print(ceasar_decipher(x[0],int(x[1])))


    # a()
    b()