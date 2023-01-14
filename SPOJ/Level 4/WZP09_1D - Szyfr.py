def decryption(string):
    n = len(string)
    mid = (n + 1) // 2
    if n < 3:
        return string
    else:
        a = string[0]
        new = string[1:mid]
        b = string[mid:]
        return decryption(new) + a + decryption(b)


print(decryption(str(input())))
