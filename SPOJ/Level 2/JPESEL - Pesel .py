def check_pesel(pesel):
  weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
  sum = 0
  for i in range(11):
    sum += int(pesel[i]) * weights[i]
  return sum % 10 == 0

n = int(input())
for i in range(n):
  print("D" if check_pesel(input()) else "N")