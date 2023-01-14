t = int(input())
for i in range(t):
    r = list(map(lambda x: int(x), input().split()))
    l = len(r)
    if l <= 1:
        print(r[1])
        continue
    for j in range(2,l,2):
        print(r[j],end=" ")
    for j in range(1,l,2):
        print(r[j],end=" ")
    print()
