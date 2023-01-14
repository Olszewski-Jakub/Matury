def dzielniki(N):
    ev_count = 0
    od_count = 0
    for i in range(1, int(pow(N, 1 / 2)) + 1):
        if (N % i == 0):
            if (i == N / i):

                if (i % 2 == 0):
                    ev_count += 1
                else:
                    od_count += 1

            else:
                if (i % 2 == 0):
                    ev_count += 1
                else:
                    od_count += 1
                if ((N / i) % 2 == 0):
                    ev_count += 1
                else:
                    od_count += 1
    return od_count == ev_count


def divisorsSame(n):
    # If (n-2)%4 is an integer, then
    # return true else return false
    return (n - 2) % 4 == 0;

def checkFactors(N):
    if N == 1:
        return 2
    czy_wywazona = False

    while not czy_wywazona:
        N += 1
        czy_wywazona = divisorsSame(N)
    return N


t = int(input())
for i in range(t):
    print(checkFactors(int(input())))
