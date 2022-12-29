r = [0]*10
while True:
    try:
        s = input().split()
        if s[0] == 'z':
            r[int(s[1])] = int(s[2])
        else:
            a,b = r[int(s[1])], r[int(s[2])]
            if s[0] == '+':
                print(a+b)
            elif s[0] == '-':
                print(a-b)
            elif s[0] == '*':
                print(a*b)
            elif s[0] == '/':
                print(a//b)
            elif s[0] == '%':
                print(a%b)
    except:
        break
