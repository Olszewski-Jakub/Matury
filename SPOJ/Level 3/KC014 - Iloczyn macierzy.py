while True:
    try:
        n = int(input())
        macierz1 = input().split()
        macierz2 = input().split()
        m1 = [[0 for i in range(n)] for i in range(n)]
        m2 = [[0 for i in range(n)] for i in range(n)]
        macierz = [[0 for i in range(n)] for i in range(n)]
        for i in range(n * n):
            m1[i // n][i % 2] = int(macierz1[i])
            m2[i // n][i % 2] = int(macierz2[i])

        

    except:
        break
