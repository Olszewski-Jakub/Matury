from math import gcd
num_cases = int(input())
for i in range(num_cases):
    a, b = map(int, input().split())
    lcm = a * b // gcd(a, b)
    print(lcm)