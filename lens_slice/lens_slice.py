toppings = ['pepperon', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2]

num_pizzas = (len(toppings))

pizzas = list(zip(prices, toppings))
pizzas.sort()

cheapest_pizza = pizzas[0]
cheapest_pizza = pizzas[-1]
three_cheapest = pizzas[:3]

print("We sell {} different kinds of pizza!".format(num_pizzas))
print(pizzas)
print(three_cheapest)