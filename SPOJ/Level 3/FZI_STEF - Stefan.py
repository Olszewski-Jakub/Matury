r = []
n = int(input())
for x in range(n):
    r.append(int(input()))


m, c = 0, 0
for i in r:
    c += i
    if c < 0:
        c = 0
    m = max(m, c)

print(m)



# m = 0
# for i in range(len(r)):
#     for j in range(len(r)):
#         s = sum(r[i:j+1])
#         if s > m:
#             m = s
# print(m)
