def factoring(a, x):
    a = 2 # factoring this out of the if statement ensures that a = 2 no matter what x is equal to
    if x < 30:
        x += 1
    print("Python is awesome!", x)
    print("a =", a)
    print("x =", x)

factoring(2, 15)