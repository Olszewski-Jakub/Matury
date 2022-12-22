while True:
    try:
        c, word = input().split()
        filtered_word = ''.join([ch for ch in word if ch != c])
        print(filtered_word)
    except:
        break

