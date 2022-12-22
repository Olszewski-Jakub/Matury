t = int(input())
for x in range(t):
   n = int(input())
   s = input(" ").split()
   sum = 0
   for x in range(len(s)):
       sum += int(s[x])
   print(sum)