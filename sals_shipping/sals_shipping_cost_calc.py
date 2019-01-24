shippingCostDict = {125.0: "Premium Ground Shipping"}


def askWeight():
  print("please input package weight")
  weight = input()

  return float(weight)


def groundShipping(weight):
  flatCharge = 20.0
  if weight <= 2.0:
    price_per_pound = 1.5
  elif 6.0 >= weight > 2.0:
    price_per_pound = 3.00
  elif 10 >= weight > 6.0:
    price_per_pound = 4.00
  else:
    price_per_pound = 4.75
  shippingCostDict.update({price_per_pound * weight + flatCharge: "Ground Shipping"})
  return price_per_pound * weight + flatCharge


def droneShipping(weight):
  if weight <= 2.0:
    price_per_pound = 4.5
  elif 6.0 >= weight > 2.0:
    price_per_pound = 9.00
  elif 10 >= weight > 6.0:
    price_per_pound = 12.00
  else:
    price_per_pound = 14.25

  shippingCostDict.update({price_per_pound * weight: "Drone Shipping"})
  return price_per_pound * weight


weight = askWeight()
groundPrice = groundShipping(weight)
dronePrice = droneShipping(weight)
minPrice = min([groundPrice, dronePrice, 125.0])

print("The cheapest option for shipping option is {} for {} at the weight of {}lb".format(shippingCostDict[minPrice],
                                                                                          minPrice, weight))
