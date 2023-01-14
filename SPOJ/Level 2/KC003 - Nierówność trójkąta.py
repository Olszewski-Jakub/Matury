def is_triangle(a, b, c):
  return a + b > c and a + c > b and b + c > a

while True:
  try:
    a, b, c = map(float, input().split())
    print(int(is_triangle(a, b, c)))
  except:
    break
