import math

# recipe makes 5 gallons of beverage
def pouches_of_hops(gallons):
  #Need 15oz oh hops, 2oz of hops for $4.20
  ounces = gallons / 5 * 15
  # pouches  = math.ceil(ounces / 2)
  pouches = (ounces + 1) // 2 #allows you to round up by adding 1 then floors the value example 15.5 + 1 = 16.5 // 2 = 16
  return pouches

def pounds_of_malt(gallons):
  # for every 5 gallons = 12.5 lbs of Malt, $1.75 per lb
  return gallons / 5 * 12.5

def packets_of_yeast(gallons):
  # every 5 gallon = 1 packet of yeast,  $3.59 each
  packets = math.ceil(gallons / 5)
  return packets

def total_cost(gallons):
  # pouches of hops are $4.20, Malt $1.75/lb, packets $3.59/ea
  pouches_cost = pouches_of_hops(gallons) * 4.20
  malt_cost = pounds_of_malt(gallons) * 1.75
  packets_cost = pounds_of_malt(gallons) * 3.59
  return pouches_cost + malt_cost + packets_cost

def main():
  my_gallons = 7
  print(pouches_of_hops(my_gallons))
  print(pounds_of_malt(my_gallons))
  print(packets_of_yeast(my_gallons))
  print(total_cost(my_gallons))

main()
# for push practice