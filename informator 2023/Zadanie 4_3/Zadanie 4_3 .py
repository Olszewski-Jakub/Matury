with open('dane4.txt') as dane:
    dane = dane.readlines()
    dane = list(map(lambda x: int(x.rstrip()), dane))

    i_par_max = 0
    index = 0
    for i in range(len(dane)):
        i_par = 0
        for j in range(0, i, 1):
            if dane[i] > dane[j]:
                i_par += 1
        if i_par > i_par_max:
            i_par_max = i_par
            index = i
    print(index+1)
