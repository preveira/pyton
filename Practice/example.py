# def bottle_verse(string, number):
#   line_one = 'bottles of beer on the wall\n'
#   line_two = 'bottles of beer\n'
#   line_three = 'Take one down, pass it around\n'
#   line_four = 'bottles of beer on the wall\n'
#   string = line_one + line_two + line_three + line_four
#   for i in range(number):
#       print(f'{str(number - i)} {string}')
# bottle_verse('', 99)

# Write a function that converst celsius to farenheight
# def celsius_to_farenheit(F):
#   celsius = (F - 32) / 9 * 5
#   print(f'{F} Degrees Farenheit is equal to approximately {round(celsius)} Degrees Celsius')
# celsius_to_farenheit(100)
# def main():
#     x = "happy"
#     y = "pumpkin"
#     z = "orange"
#     pumpkin = "sleepy"
#     happy = "vampire"

#     orange(y, x, z)
#     orange(x, z, y)
#     orange(pumpkin, z, "y")
#     z = "green"
#     orange("x", "pumpkin", z)
#     orange(y, z, happy)

# def orange(z, y, x):
#     print(y + " and " + z + " were " + x)

# main()

# Write a function named factorial that accepts an integer n as a parameter and prints the factorial of n, or n!, as output. A factorial of an integer is defined as the product of all integers from 1 through that integer inclusive. For example, the call of factorial(4) should print the following output:

# 4 factorial = 24
# The factorial of 0 and 1 are defined to be 1. You may assume that the value passed is non-negative and that its factorial can fit in the range of type int.

# def factorial(n):
#     result = 1
#     for i in range(n):
#         result = result * (i+1)
#         print(f'{i+1} factorial = {result}')
# factorial(4)

# Write a function named sum_up_to function that accepts an integer parameter n and returns the sum of the integers from 1 through n inclusive. For example, sum_up_to(5) returns 1 + 2 + 3 + 4 + 5 or 15. You may assume that the value of n is at least 1.

# def sum_up_to(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += i
#     return total
# result = sum_up_to(5)
# print(result)

# def hamburger(y, z, x):
#     print(z, "and", x, "like", y)
#     return z

# def main():
#     x = "Python"
#     y = "tyler"
#     z = "tv"
#     rugby = "hamburger"
#     Python = "donnie"

#     hamburger(x, y, z)
#     hamburger(z, x, y)
#     hamburger("rugby", z, Python)
#     y = hamburger(y, rugby, "x")
#     hamburger(y, y, "Python")

# main()

