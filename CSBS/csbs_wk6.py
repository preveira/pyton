def number_loops(n):
  for row in range(n):
    for col in range(5 - row - 1): #print leading periods
      print('.', end='')
    print(row + 1, end='') # print the row
    for col in range(row):
      print('.', end='') # print the trailing periods\
    print() #skip to the next line
number_loops(5)
