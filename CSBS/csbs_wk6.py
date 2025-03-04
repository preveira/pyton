def number_loops(n):
  for row in range(n):
    for col in range(5 - row - 1): #print leading periods
      print('.', end='')
    print(row + 1, end='') # print the row
    for col in range(row):
      print('.', end='') # print the trailing periods\
    print() #skip to the next line
number_loops(5)

def number_square(min, max):
  for row in range(min, max + 1):
    number_to_print = row
    for col in range(max - min + 1):
      if number_to_print > max:
        number_to_print = min
      print(number_to_print, end='')
      number_to_print += 1
    print()

number_square(1, 5)

def number_square2(min, max):
  base = max - min + 1
  for row in range(max - min + 1):
    for col in range(max - min + 1):
      print(min + (row + col) % base, end='')
    print()

number_square2(1, 5)