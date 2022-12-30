t = int(input())
for i in range(t):
    s1, s2 = input(), input()
    z = False
    for x in range(len(s1)):
        s = s1[x::] + s1[0:x:1]
        if s == s2:
            z = True
            break
    print("yes" if z else "no")
