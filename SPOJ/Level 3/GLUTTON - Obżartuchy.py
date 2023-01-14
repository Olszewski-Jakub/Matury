from math import ceil

t = int(input())
k = 0
while t > k:
    k += 1
    DOBA = 86400
    nums = input().split()
    n = int(nums[0])
    pud = int(nums[1])
    tab = []
    ciastka = []
    suma = 0
    for i in range(0, n, 1):
        tab.insert(i, int(input()))
        ciastka.insert(i, int(DOBA / tab[i]))
        # suma=ciastka[0]
        suma += ciastka[i]
    print(int(ceil(suma / pud)))
