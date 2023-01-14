import re
from string import ascii_letters
import collections

with open('hasla.txt') as hasla:
    hasla = hasla.readlines()
    hasla = list(map(lambda x: x.rstrip(), hasla))


    # print(hasla)
    def a():
        c = 0
        for x in hasla:
            c += not re.search('[a-zA-Z]', x)
        print(c)


    def b():
        print([item for item, count in collections.Counter(hasla).items() if count > 1])


    def ciag_znakow(x):
        if len(x) < 4:
            return False
        for y in range(len(x) - 3):
            r = [ord(x[y]), ord(x[y + 1]), ord(x[y + 2]), ord(x[y + 3])]
            r.sort()
            if r[0] == r[1] - 1 == r[2] - 2 == r[3] - 3:
                return True
        return False


    def c():
        c = 0
        for x in hasla:
            c += ciag_znakow(x)
        print(c)


    def d():
        c = 0
        for x in hasla:
            c += bool(re.search('[0-9]',x)) and bool(re.search('[a-z]',x)) and bool(re.search('[A-Z]',x))
        print(c)

    a()
    b()
    c()
    d()
