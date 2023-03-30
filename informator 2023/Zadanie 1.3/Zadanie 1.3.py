with open('dane1_3.txt') as dane:


    segment_max = 0
    # print(dane)
    for x in range(len(dane)):
        for y in range(len(dane)):
            temp = sum(dane[x:y+1])
            segment_max = max(temp,segment_max)
    print(segment_max)
