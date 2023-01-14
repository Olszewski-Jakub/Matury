from string import ascii_letters
t = int(input())
letter_count = {}
for i in range(t):
    text = input().replace(" ","")

    for c in text:
        if c not in letter_count:
            letter_count[c] = 1
        else:
            letter_count[c] += 1

for c in ascii_letters:
    if c in letter_count:
        print(f'{c} {letter_count[c]}')
