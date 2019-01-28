import os

cwd = os.getcwd()
daily_sales = open(cwd + "/thread_shed_data.txt").read()

print(daily_sales)