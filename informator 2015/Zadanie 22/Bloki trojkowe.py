import timeit
with open('bloki1.txt') as bloki1, open('bloki2.txt') as bloki2, open('bloki3.txt') as bloki3:
    bloki1 = bloki1.readlines()
    bloki1 = list(map(lambda x: int(x.rstrip()), bloki1))
    bloki2 = bloki2.readlines()
    bloki2 = list(map(lambda x: int(x.rstrip()), bloki2))
    bloki3 = bloki3.readlines()
    bloki3 = list(map(lambda x: int(x.rstrip()), bloki3))


    # print(bloki3)
    # print(bloki1)
    # print(bloki2)

    def find_triple_blocks(blok):
        m_len = 0
        for i in range(len(blok)):
            for j in range(i, len(blok), 1):
                if sum(blok[i:j + 1]) % 3 == 0:
                    m_len = max(m_len, j + 1 - i)
        print(m_len)


    def find_triple_blocks_v2(a):
        n = len(a)
        triple_blocks = 0
        for i in range(n):
            for j in range(i, n):
                block = a[i:j + 1]
                divisible_by_3 = sum(1 for x in block if x % 3 == 0)
                if divisible_by_3 > len(block) / 2:
                    triple_blocks += 1
        return triple_blocks


    def find_triple_blocks_v3(a):
        n = len(a)
        triple_blocks = 0
        processed_blocks = 0
        total_blocks = (n * (n + 1)) / 2
        for i in range(n):
            for j in range(i, n):
                block = a[i:j + 1]
                divisible_by_3 = sum(1 for x in block if x % 3 == 0)
                if divisible_by_3 > len(block) / 2:
                    triple_blocks += 1
                processed_blocks += 1
                if processed_blocks % 1000 == 0:
                    print("Progress: {:.2f}%".format(processed_blocks / total_blocks * 100))
        return triple_blocks


    def find_triple_blocks_v4(a):
        n = len(a)
        triple_blocks = 0
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + a[i - 1]

        for i in range(n):
            for j in range(i, n):
                block = a[i:j + 1]
                divisible_by_3 = sum(1 for x in block if x % 3 == 0)
                if divisible_by_3 > len(block) / 2:
                    triple_blocks += 1
        return triple_blocks


    def find_triple_blocks_v6(a):
        n = len(a)
        count = 0
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + a[i - 1]
        for i in range(n):
            for j in range(i, n):
                block = a[i:j + 1]
                divisible_by_3 = sum(1 for x in block if x % 3 == 0)
                if divisible_by_3 > len(block) / 3:
                    count += 1
        return count


    print(find_triple_blocks(bloki1))