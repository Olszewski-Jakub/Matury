with open('dane8.txt') as dane:
    dane = dane.readlines()
    dane = list(map(lambda x: int(x.rstrip()), dane))

    def a():
        parzyste, nieparzyste = 0,0
        for x in range(len(dane)-1):
            if abs(dane[x]-dane[x+1]) % 2 ==0:
                parzyste +=1
            else:
                nieparzyste += 1
        print(parzyste,nieparzyste)

    def b():
        nieuporzadkowane = 0
        for x in range(len(dane) - 1):
            for y in range(x, len(dane)):
                if dane[x] > dane[y]:
                    nieuporzadkowane +=1

        print(nieuporzadkowane)


    def c():
        ciag_max = 0
        count = 1
        for x in range(1,len(dane)):
            if dane[x-1] < dane[x]:
                count +=1
            else:
                if count>ciag_max:
                    ciag_max = count
                count = 1
        print(ciag_max)

    a()
    b()
    c()