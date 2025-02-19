def has_midpoint(a, b, c):
  return a == (b+c)/2 or b == (a+c)/2 or c == (a+b)/2

print(has_midpoint(4,6,8))
print(has_midpoint(3,1,3))

# code passed problem set and test
import random

def give_problems(n):
  for i in range(n):
    x = random.randint(1,12)
    y = random.randint(1,12)
    prompt = int(input(f"{x} x {y} = "))
    if prompt == x * y:
      print('Correct')
    else:
      print(f'Incorrect, the answer was {x*y}')
give_problems(3)