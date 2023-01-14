def number_to_text(n):
    if n < 0:
        return "minus " + number_to_text(-n)
    if n == 0:
        return "zero"

    units = ["", "jeden", "dwa", "trzy", "cztery", "pięć", "sześć", "siedem", "osiem", "dziewięć"]
    teens = ["", "jedenaście", "dwanaście", "trzynaście", "czternaście", "piętnaście", "szesnaście", "siedemnaście", "osiemnaście", "dziewiętnaście"]
    tens = ["", "dziesięć", "dwadzieścia", "trzydzieści", "czterdzieści", "pięćdziesiąt", "sześćdziesiąt", "siedemdziesiąt", "osiemdziesiąt", "dziewięćdziesiąt"]
    hundreds = ["", "sto", "dwieście", "trzysta", "czterysta", "pięćset", "sześćset", "siedemset", "osiemset", "dziewięćset"]

    trilions = n // 1_000_000_000_000
    billions = (n % 1_000_000_000_000) // 1_000_000_000
    millions = (n % 1_000_000_000) // 1_000_000
    thousands = (n % 1_000_000) // 1_000
    rest = n % 1000

    result = ""
    if trilions > 0:
        result += number_to_text(billions) + " bln. "
    if billions > 0:
        result += number_to_text(billions) + " mld. "
    if millions > 0:
        result += number_to_text(millions) + " mln. "
    if thousands > 0:
        result += number_to_text(thousands) + " tys. "
    if rest > 0:
        if billions + millions + thousands > 0:
            result += "i "
        if rest >= 100:
            result += hundreds[rest // 100] + " "
            rest %= 100
        if rest >= 20:
            result += tens[rest // 10 ] + " "
            rest %= 10
        if rest > 0:
            if rest >= 11 and rest <= 19:
                result += teens[rest - 11] + " "
            else:
                result += units[rest] + " "

    return result.strip()


t = int(input())
for i in range(t):
    print(number_to_text(int(input())))