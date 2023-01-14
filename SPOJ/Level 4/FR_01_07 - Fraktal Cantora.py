import math

def cantor(n):
    len = int(math.pow(3, n-1)) # obliczamy długość linii
    cantor = ['_' for i in range(len)] # tworzymy pierwszą linię
    print(''.join(cantor)) # wypisujemy pierwszą linię osobno
    for i in range(1, n):
        nonempty = 0
        for j in range(len):
            if cantor[j] == ' ':
                for k in range(int(nonempty/3)):
                    cantor[j-int(2*nonempty/3)+k] = ' '
                nonempty = 0
            else:
                nonempty += 1
        for k in range(int(nonempty/3)):
            cantor[len-int(2*nonempty/3)+k] = ' '
        print(''.join(cantor))

t = int(input())
for i in range(t):
    n = int(input())
    cantor(n)
    if i < t-1:
        print()
