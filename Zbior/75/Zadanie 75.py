with open('probka.txt') as probka, open('tekst.txt') as tekst:
    tekst = tekst.readline().rstrip().split()
    probka = probka.readlines()
    probka = list(map(lambda x: x.rstrip().split(), probka))


    def a():
        c = 0
        for x in tekst:
            if x[0] == x[-1] == 'd':
                print(x)
        print()


    def affine_cipher(text, A, B):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        mapping = {letter: num for num, letter in enumerate(alphabet)}
        encrypted_text = ''
        for letter in text:
            num = (A * mapping[letter] + B) % 26
            encrypted_text += alphabet[num]
        return encrypted_text


    def affine_decipher(ciphertext, A, B):
        # Create the mapping of letters to numbers
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        mapping = {letter: num for num, letter in enumerate(alphabet)}
        # Decrypt the text
        decrypted_text = ''
        # find A^-1
        A_inv = None
        for i in range(1, 26):
            if (A * i) % 26 == 1:
                A_inv = i
                break
        if A_inv is None:
            return 0
        for letter in ciphertext:
            num = (A_inv * (mapping[letter] - B)) % 26
            decrypted_text += alphabet[num]
        return decrypted_text


    def b():
        for x in tekst:
            if len(x) >= 10:
                print(affine_cipher(x,5,2))



    def c1(x,y):
        if x == y:
            return 0,0
        for A in range(0,26):
            for B in range(0,26):
                if affine_cipher(x,A,B) == y:
                    return A,B
    def c2(x,y):
        if x == y:
            return 0,0
        for A in range(1,26):
            for B in range(1,26):
                if affine_decipher(y,A,B) == x:
                    return A,B
    def c():
        for x,y in probka:

            print(f"Klucz szyfrujący {c1(x,y)}")
            print(f"Klucz deszyfrujący {c2(x,y)}")
            print()


    a()
    b()
    c()

