def has_midpoint(a, b, c):
  return a == (b+c)/2 or b == (a+c)/2 or c == (a+b)/2

print(has_midpoint(4,6,8))
print(has_midpoint(3,1,3))

# code passed problem set and test
import random

#allows you to generate (n) numbers of multiplication problems with numbers between 1-12.
def give_problems(n):
  for i in range(n):
    x = random.randint(1,12)
    y = random.randint(1,12)
    prompt = int(input(f"{x} x {y} = "))
    if prompt == x * y:
      print('Correct')
    else:
      print(f'Incorrect, the answer was {x*y}')
  print(f'{n} Problems Solved.')
give_problems(3)

# reassignment of values practice. Follow the order of things (1st, 2nd, 3rd). then where they print(2nd, 1st, 3rd) <-- example
def main():
  hear = 'bon'
  song = 'merde'
  merde = 'hear'
  walk = 'run'
  run = 'feel'
  feel = 'walk'

  claim(feel, song, feel)
  claim(merde, hear, song)
  claim(run, "song", feel)
  claim('claim', run , walk)
  claim(run, 'bon', walk)

def claim(hear, merde, song):
  print('to', hear, 'the', song, 'is', merde) 
main()