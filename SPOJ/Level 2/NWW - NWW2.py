def najmniejsza_wspolna_wielokrotnosc(a):
  M = max(a)
  while True:
    dzieli_wszystkie = True
    for x in a:
      if M % x != 0:
        dzieli_wszystkie = False
        break
    if dzieli_wszystkie:
      return M
    M += 1

t = int(input())

for i in range(t):
  n = int(input())
  a = list(map(int, input().split()))
  m = najmniejsza_wspolna_wielokrotnosc(a)
  print(m)