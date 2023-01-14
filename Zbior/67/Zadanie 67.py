from math import sqrt

def Fibonacci(n):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

def fibonacci_nums(n):
  if n <= 0:
    return [0]
  sequence = [0, 1]
  while len(sequence) <= n:
    next_value = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
    sequence.append(next_value)
  return sequence


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    return True

def a():
    for x in [10,20,30,40]:
        print(Fibonacci(x))

first_40 = fibonacci_nums(40)

def b():
    for x in first_40:
        if is_prime(x):
            print(x)

def c():

    for x in first_40:
        print(bin(x).lstrip("0b"))

def d():
    for x in first_40:
        if (y:=bin(x).lstrip("0b")).count('1') == 6:
            print(y)
d()