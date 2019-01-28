import os

cwd = os.getcwd()
daily_sales = open(cwd + "/thread_shed_data.txt").read()
daily_sales_replaced = daily_sales.replace(";,;", "|")
daily_transactions = daily_sales_replaced.split(",")
daily_transactions_split = [split_str.split("|") for split_str in daily_transactions]
transactions_clean = []

for item_list in daily_transactions_split:
  clean_list = []
  for string in item_list:
    if '"""' in string:
      clean_list.append(string.replace('"""', '').strip())
    else:
      clean_list.append(string.strip())
  transactions_clean.append(clean_list)

customers = []
sales = []
thread_sold = []
date = []

for item_list in transactions_clean:
  customers.append(item_list[0])
  sales.append(item_list[1])
  thread_sold.append(item_list[2])
  date.append(item_list[3])


total_sales = 0

for sale_price in sales:
  total_sales += float(sale_price[1:])

thread_sold_split = []

for thread_color in thread_sold:
  if "&" in thread_color:
    thred_split = thread_color.split("&")
    thread_sold_split.append(thred_split[0])
    thread_sold_split.append(thred_split[1])
  else:
    thread_sold_split.append(thread_color)

def color_count(color):
  count = 0
  for thread_color in thread_sold_split:
    if color == thread_color:
      count += 1
  return count



colors = ['red', 'yellow', 'green', 'white', 'black', 'blue', 'purple']

for color in colors:
  print("{_COLOR_COUNT}, {_COLOR} colored thread has been sold today.".format(_COLOR_COUNT=color_count(color), _COLOR=color))