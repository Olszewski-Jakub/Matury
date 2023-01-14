import decimal

t = int(input())
for i in range(t):
    a, b, c, k = map(int, input().split())
    decimal.getcontext().prec = k + 20
    delta = decimal.Decimal(b * b - 4 * a * c)
    if delta > 0:
        x1 = decimal.Decimal((-b + decimal.Decimal(delta ** 0.5)) / decimal.Decimal(2 * a))
        x2 = decimal.Decimal((-b - decimal.Decimal(delta ** 0.5)) / decimal.Decimal(2 * a))

        if x1 < x2:
            print(f"2 {x1} {x2}")
        else:
            print(f"2 {x2} {x1}")
    elif delta == 0:
        x = decimal.Decimal(-b / decimal.Decimal(2 * a))
        print(f"1 {x}")
    else:
        x = 0
        print("0")
