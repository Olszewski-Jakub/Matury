s = 0
while True:
    try:
        s += int(input().replace(" ",""))
    except:
        break
print(s)
