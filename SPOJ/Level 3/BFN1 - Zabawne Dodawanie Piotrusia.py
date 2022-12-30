t = int(input())
for i in range(t):
    s = input()
    c = 0
    if s == s[::-1]:
        print(s, 0)
        continue
    while s != s[::-1]:
        temp = int(s) + int(s[::-1])
        s = str(temp)
        c += 1
    print(s,c)