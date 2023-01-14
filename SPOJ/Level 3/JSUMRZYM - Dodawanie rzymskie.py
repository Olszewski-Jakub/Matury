def roman_to_arabic(roman):
    roman_to_arabic_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    result = 0
    prev_value = float("inf")
    for c in reversed(roman):
        value = roman_to_arabic_map[c]
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value
    return result

def arabic_to_roman(arabic):
    arabic_to_roman_map = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]
    result = ""
    for value, roman in arabic_to_roman_map:
        while arabic >= value:
            arabic -= value
            result += roman
    return result

def add_roman(roman1, roman2):
    arabic1 = roman_to_arabic(roman1)
    arabic2 = roman_to_arabic(roman2)
    arabic_result = arabic1 + arabic2
    roman_result = arabic_to_roman(arabic_result)
    return roman_result

# testy
print(add_roman("I", "I"))
print(add_roman("I", "V"))
print(add_roman("X", "L"))
print(add_roman("C", "D"))
print(add_roman("M", "M"))
