# def number_loops(n):
#   for row in range(n):
#     for col in range(5 - row - 1): #print leading periods
#       print('.', end='')
#     print(row + 1, end='') # print the row
#     for col in range(row):
#       print('.', end='') # print the trailing periods\
#     print() #skip to the next line
# number_loops(5)

# def number_square(min, max):
#   for row in range(min, max + 1):
#     number_to_print = row
#     for col in range(max - min + 1):
#       if number_to_print > max:
#         number_to_print = min
#       print(number_to_print, end='')
#       number_to_print += 1
#     print()

# number_square(1, 5)

# def number_square2(min, max):
#   base = max - min + 1
#   for row in range(max - min + 1):
#     for col in range(max - min + 1):
#       print(min + (row + col) % base, end='')
#     print()

# number_square2(1, 5)

# def sentinel_min_max():
#   prompt = 'Type a number (or -1 to stop): '
#   user_input = int(input(prompt))
#   if user_input != -1:
#     min = user_input
#     max = user_input
#     while user_input != -1:
#       user_input = int(input(prompt))
#       if user_input > max:
#         max = user_input
#       if user_input != -1 and user_input < min:
#         min = user_input
#     print('Maximum was', max)
#     print('Minimum was', min)
#   sentinel_min_max()

# def roll_two_dice():

# def loop_mystery_exam1(i, j):
#     while i != 0 and j != 0:
#         i = i // j
#         j = (j - 1) // 2
#         print(str(i) + " " + str(j) + " ", end="")
#     print(str(i))
#     return i + j

# loop_mystery_exam1(1600, 40)

# def loop_mystery_exam3(x, y):
#     z = x + y
#     while x > 0 and y > 0:
#         x = x - y
#         y -= 1
#         print(str(x) + " " + str(y) + " ", end="")
#     print(str(y))
#     return z

# loop_mystery_exam3(40, 10)

# def compute_sum_of_digits():
#   digit_sum = 0
#   n = int(input("Type an integer: "))
#   while n > 0:
#     last_digit = n % 10
#     digit_sum += last_digit
#     n //= 10
#   print(f'Digit sum is {digit_sum}')
# compute_sum_of_digits()

# import random

# def roll_two_dice():
#   dice_one = random.randint(1,6)
#   dice_two = random.randint(1,6)
#   user_input = int(input("Desired sum:"))
#   print(f"{dice_one} and {dice_two} = {dice_one + dice_two}")
#   while dice_one + dice_two != user_input:
#     dice_one = random.randint(1,6)
#     dice_two = random.randint(1,6)
#     print(f"{dice_one} and {dice_two} = {dice_one + dice_two}")
# roll_two_dice()

# def gcd(A, B):
#   if B == 0:
#     return abs(A)
#   return gcd(B, A % B)

def print_average():
  count = 0
  total = 0
  user_input = int(input("Type a number: "))
  if user_input > 0:
    count += 1
    total += user_input
  while user_input > 0:
    user_input = int(input("Type a number: "))
    if user_input > 0:
      count += 1
      total += user_input
  if count > 0:
    print(f'Average was {total / count}')
print_average()