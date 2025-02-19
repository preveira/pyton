# function to compute the area of a circle
import math

def area(r):
  area = math.pi*r**2
  return area


def compute_distance(x1, y1, x2, y2):
  return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def count_digits(n):
  return len(str(abs(n))) #this calculates the length by converting to a string and uses abs(n) to convert to to a positive number before converting to a 'string' which gets rid of the negative(-) symbol.

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(f"{n} factorial = {result}")

def get_first_digit(n):
   return int(str(abs(n))[0]) #This does alsmot the same as count_digit() above but at the end it grabs the value at the [0] index position.

def get_last_digit(n):
   return int(str(abs(n))[-1])

def sum_of_digits(n):
    n = abs(n)
    result = 0
    while n > 0:
        result += n % 10  
        n //= 10  
    return result