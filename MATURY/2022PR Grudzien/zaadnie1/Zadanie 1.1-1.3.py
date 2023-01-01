with open('mecz_przyklad.txt') as przyklad, open('mecz.txt') as mecze, open('wyniki1.txt', "w") as wyniki:
    przyklad = przyklad.readline()
    mecze = mecze.readline()

    dane = mecze


    def a():
        c = dane.count("AB") + dane.count("BA")
        print(f"zadanie 1.1 {c}", file=wyniki)


    def b():
        c_a, c_b = 0, 0
        for x in dane:
            c_a += x == 'A'
            c_b += x == 'B'
            if c_a >= 1000 and c_a - c_b >= 3:
                print(f"zadanie 1.2 A {c_a}:{c_b}",file=wyniki)
                break
            if c_b >= 1000 and c_b - c_a >= 3:
                print(f"zadanie 1.2  B {c_a}:{c_b}",file=wyniki)
                break



    def c():
        najdluzszy = 0
        max_druzyna = ""
        druzyna = ""
        ilosc_pass = 0
        licznik = 0
        for x in range(len(dane)-1):
            if dane[x] == dane[x+1]:
                licznik += 1
                druzyna = dane[x]
            else:
                if licznik >= 10:
                    ilosc_pass += 1
                if licznik>najdluzszy:
                    najdluzszy = licznik
                    max_druzyna = druzyna
                licznik = 1

        print(f"zadanie 1.3 \nilość pass: {ilosc_pass}\ndruzyna: {max_druzyna}\ndlugość: {najdluzszy}", file=wyniki)

    a()
    b()
    c()
