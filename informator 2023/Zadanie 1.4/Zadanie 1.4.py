with open('dane1_4.txt') as dane:
    dane = dane.readlines()
    dane = list(map(lambda x: int(x.rstrip()), dane))

    pocz = 0
    max_pocz = 0
    max_kon = 0
    suma  = 0
    suma_max = 0
    for i in range(len(dane)):
        suma += dane[i]
        if suma < 0:
            suma=0
            pocz = i+1
        if suma > suma_max:
            suma_max = suma
            max_pocz = pocz
            max_kon = i
    print(max_pocz+1,max_kon+1)

