stack = []

while True:
    try:
        # Wczytujemy polecenie
        command = input()
        if command == '+':
            # Wstawienie liczby na stos
            value = int(input())
            if len(stack) < 10:
                stack.append(value)
                print(':)')
            else:
                print(':(')
        elif command == '-':
            # Zdjęcie liczby ze stosu
            if stack:
                value = stack.pop()
                print(value)
            else:
                print(':(')
    except:
        break