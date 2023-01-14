def wyszukiwanie(r, S):
    L = 0
    R = len(r) - 1
    while L <= R:
        x = (L + R) // 2
        if r[x] == S:
            return True
        elif r[x] > S:
            R = x - 1
        else:
            L = x + 1
    return False

input()
r = [int(x) for x in input().split()]
t = int(input())
for i in range(t):
    if wyszukiwanie(r,int(input())):
        print("TAK")
    else:
        print("NIE")