# t = int(input())
# for i in range(t):
#     r = input().split()
#     a,b = int(r[0]), int(r[1])
#     if a == b:
#         print(a+b)
#         continue
#     while a!=b:
#         if a<b:
#             b -= a
#         else:
#             a -= b
#     print(a+b)
t = int(input())
for i in range(t):
    r = input().split()
    a, b = int(r[0]), int(r[1])
    if a == b:
        print(a + b)
        continue
    while b != 0:
        r = a % b
        a = b
        b = r   

    print(2 * a)
