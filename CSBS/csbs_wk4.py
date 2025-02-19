# def factoring(a, x):
#     a = 2 # factoring this out of the if statement ensures that a = 2 no matter what x is equal to
#     if x < 30:
#         x += 1
#     print("Python is awesome!", x) #factored out the print function to avoind redundancy in the origional if/else statement
#     print("a =", a)
#     print("x =", x)

# factoring(2, 15)

# def mystery(n):
#     if n < 0:
#         n = n * 3
#         print(n)
#     else:
#         n = n + 3
#         if n % 2 == 1:
#             n = n + n % 10
#         print(n)

# mystery(-5)
# mystery(0)
# mystery(7)
# mystery(18)
# mystery(49)

def if_else_mystery_1(x, y):
    z = 4
    if z <= x:
        z = x + 1
    else:
        z = z + 9
    if z <= y:
        y += 1
    print(z, y)

if_else_mystery_1(3, 20)
if_else_mystery_1(4, 5)
if_else_mystery_1(5, 5)
if_else_mystery_1(6, 10)