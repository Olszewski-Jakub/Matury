def encrypt_caesar(text):
    result = ""
    for ch in text:
        if ch == ' ':
            result += ch
        elif ch == '\n':
            result += ch
        else:
            result += chr((ord(ch) - ord('A') + 3) % 26 + ord('A'))
    return result

while True:
    try:
        print(encrypt_caesar(input()))
    except:
        break
