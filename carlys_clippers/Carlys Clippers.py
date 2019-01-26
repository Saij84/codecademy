hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price = 0
total_revenue = 0

new_prices = [price-5 for price in prices]

average_daily_revenue = total_revenue/7

for price in prices:
  total_price += price

for i in range(len(hairstyles)):
  total_revenue += (prices[i]*last_week[i])

average_price = total_price/len(prices)

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[1] < 30]

print("Average Haircut Price:\n{}".format(average_price))
print(new_prices)
print("Total Revenue: {}".format(total_revenue))
print(cuts_under_30)


