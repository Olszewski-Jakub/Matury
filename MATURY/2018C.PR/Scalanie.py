with open('dane1.txt') as dane1, open('dane2.txt') as dane2, open('przyklad1.txt') as przyklad1, open(
        'przyklad2.txt') as przyklad2:
    r = [dane1, dane2, przyklad1, przyklad2]
    ciagi = []
    for x in r:
        x = x.readlines()
        x = list(map(lambda x: list(map(int, x.rstrip().split())), x))
        # print(x)
        ciagi.append(x)

    c1,c2 = ciagi[0],ciagi[1]
    # c1, c2 = ciagi[2], ciagi[3]


    # print(c1, c2)

    def a():
        c = 0
        for x in range(len(c1)):
            c += c1[x][-1] == c2[x][-1]
        print(c)


    def b1(x):
        odd, even = 0, 0
        for y in x:
            if y % 2 == 0:
                even += 1
            else:
                odd += 1
        return even == 5 and odd == 5


    def b():
        # dla c1
        odd_c1, even_c1, odd_c2, even_c2 = 0, 0, 0, 0
        c = 0
        for x in range(len(c1)):
            c += b1(c1[x]) and b1(c2[x])
        print(c)


    def liczby(c):
        r = []
        for x in c:
            r.append(x)
        return set(r)


    def c():
        for x in range(len(c1)):
            if liczby(c1[x]) == liczby(c2[x]):
                print(x + 1, end=" ")
        print()


    def d():
        for c in range(len(c1)):
            numbers1 = c1[c]
            numbers2 = c2[c]
            merged_list = []

            i, j = 0, 0
            while i < len(numbers1) and j < len(numbers2):
                if numbers1[i] <= numbers2[j]:
                    merged_list.append(numbers1[i])
                    i += 1
                else:
                    merged_list.append(numbers2[j])
                    j += 1

            while i < len(numbers1):
                merged_list.append(numbers1[i])
                i += 1

            while j < len(numbers2):
                merged_list.append(numbers2[j])
                j += 1

            print(*merged_list)



    a()
    b()
    c()
    d()