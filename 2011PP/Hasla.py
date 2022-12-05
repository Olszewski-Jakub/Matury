def ascii_sum(x):
    for y in range(len(x) - 1):
        if ord(x[y]) + ord(x[y+1]) == 220:
            return True
    return False


with open('hasla.txt') as hasla:
    hasla = hasla.readlines()
    hasla = list(map(lambda x: x.rstrip(), hasla))
    # print(hasla)

    #a)
    par, niepar = 0, 0
    for x in hasla:
        if len(x) % 2 == 0:
            par += 1
        else:
            niepar += 1

    print(f"Parzyste {par}\nNIe parzyste {niepar}\n\n")

    #b)
    r = []
    for x in hasla:
        if x == x[::-1]:
            print(x)

    print("\n\n")

    # c)
    for x in hasla:
        if ascii_sum(x):
            print(x)

