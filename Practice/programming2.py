def average(n):
  sum = 0
  for i in range(1, n + 1):
    sum += i
  return print(sum/n)
for i in range(1, 11):
  result = average(i)
average(3)

# mortgage calculator


# P = 30000 # principal
# apr = 5.84 # annual percenage rate
# r = apr/12/100 # r is the mothly interest rate
# y = 4 # term in years
# N = y*12 # number of months
# c = r*P/(1-(1+r)**(-N)) # monthly payment

# print(f"monthly payment:{c:.2f}")
# balance = P
# for mm in range(1, N + 1):
#   interest = balance * r
#   principal = c - interest
#   balance = balance - principal
#   print(f"'month:'{mm}, 'intesrest:'{interest:.2f}, 'principal:'{principal:.2f}, 'balance:'{balance:.2f}")
