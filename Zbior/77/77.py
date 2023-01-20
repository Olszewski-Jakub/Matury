def VigenereCipher(plainText, key, encrypt=True):
    key = key.upper()
    key_len = len(key)
    key_ascii = [ord(i) for i in key]
    plainText = plainText.upper()
    plainText_len = len(plainText)
    plainText_ascii = [ord(i) for i in plainText]
    if encrypt:
        cipherText = ""
        for i in range(plainText_len):
            x = (plainText_ascii[i] + key_ascii[i % key_len]) % 26
            x += ord('A')
            cipherText += chr(x)
    else:
        cipherText = ""
        for i in range(plainText_len):
            x = (plainText_ascii[i] - key_ascii[i % key_len] + 26) % 26
            x += ord('A')
            cipherText += chr(x)
    return cipherText

# zadanie 1
with open("dokad.txt", "r") as we:
    plainText = we.readline()
key = "LUBIMYCZYTAC"
cipherText = VigenereCipher(plainText, key)
print("Ciphertext: ", cipherText)

# zadanie 2
with open("szyfr.txt", "r") as f:
    cipherText = f.readline()
    key = f.readline()
plainText = VigenereCipher(cipherText, key, encrypt=False)
print("Plaintext: ", plainText)

# zadanie 3
s = plainText
L = [0] * 26
n = 0
for i in range(len(s)):
    if s[i].isalpha() and s[i].isupper():
        j = ord(s[i]) - ord('A')
        L[j] += 1
        n += 1

print(f"{n} liter w tresci szyfru")
print("Liczniki wystapien liter:")
for j in range(26):
    print(f"{chr(j + ord('A'))} - {L[j]}")

suma = 0
for j in range(26):
    suma += L[j]*(L[j]-1)
ko = suma/n/(n-1)
d = 0.0285/(ko-0.0385)

d += 0.005
d = 0.01*int(100*d)
print(f"{d} - szacunkowa dlugosc klucza")
print(f"{len(key)} - dokladna dlugosc klucza")

