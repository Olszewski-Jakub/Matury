# n, k = map(int, input().split())
#
# elements = list(map(int, input().split()))
# shifted_elements = elements[k % n:] + elements[:k % n]
#
# # Print the shifted array
# print(*shifted_elements)

n, k = map(int, input().split())
elements = list(map(int, input().split()))

for i in range(k % n):
    elements.append(elements.pop(0))
print(*elements)