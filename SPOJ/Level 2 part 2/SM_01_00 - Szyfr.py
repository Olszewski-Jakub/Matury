t  = int(input())
for i in range(t):
    s = input()
    p = ""
    for j in range(0,len(s),5):
        a = s[j:j+5]
        p += chr(int(a,2)+ord("A"))
    print(p)