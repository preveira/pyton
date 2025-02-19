def has_midpoint(a, b, c):
  return a == (b+c)/2 or b == (a+c)/2 or c == (a+b)/2

print(has_midpoint(4,6,8))
print(has_midpoint(3,1,3))

# code passed problem set and test