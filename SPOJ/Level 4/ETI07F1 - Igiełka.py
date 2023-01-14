import sys
def backpack_01(n, A, B, tents):
    F = [[[0 for k in range(B + 1)] for j in range(A + 1)] for i in range(n + 1)]

    for i in range(1, n+1):
        for j in range(1, A+1):
            for k in range(1, B+1):
                if j >= tents[i-1][0] and k >= tents[i-1][1]:
                    F[i][j][k] = max(F[i-1][j][k], F[i-1][j-tents[i-1][0]][k-tents[i-1][1]] + 1)
                else:
                    F[i][j][k] = F[i-1][j][k]
    return F[n][A][B]

def backpack_01_v2(n, A, B, tents):
    F = [[0 for j in range(B + 1)] for i in range(A + 1)]
    for i in range(1, n+1):
        for j in range(A, 0, -1):
            for k in range(B, 0, -1):
                if j >= tents[i-1][0] and k >= tents[i-1][1]:
                    F[j][k] = max(F[j][k], F[j-tents[i-1][0]][k-tents[i-1][1]] + 1)
    return F[A][B]

r = input().split()
A = int(r[1])
B = int(r[2])
n = int(r[0])
tents = []
for i in range(n):
    # temp = input().split()
    # tents.append([int(temp[0]), int(temp[1])])
    tents.append([int(x) for x in sys.stdin.readline().split() ])
print(backpack_01_v2(n,A,B,tents))

