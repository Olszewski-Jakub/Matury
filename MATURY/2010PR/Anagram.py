def a(x):
    b = len(x[0])
    for y in range(len(x)):
        if b != len(x[y]):
            return False
    return True


def anagram_(a):
    r = [0] * 26
    for x in range(len(a[0])):
        r[ord(a[0][x]) - ord('a')] += 1
    for x in a:
        l = [0] * 26
        for y in range(len(x)):
            l[ord(x[y])-ord('a')] += 1
        if r != l:
            return False
    return True

with open('anagram.txt') as anagram, open("odp_4a.txt", "w") as opd_a,open("odp_4b.txt", "w") as opd_b:
    anagram = anagram.readlines()
    anagram = list(map(lambda x: x.rstrip().split(), anagram))
    # print(anagram)

    # a)
    for x in anagram:
        if a(x):
            opd_a.write(f"{' '.join(x)}\n")

    # b)
    for x in anagram:
        if anagram_(x):
            opd_b.write(f"{' '.join(x)}\n")

