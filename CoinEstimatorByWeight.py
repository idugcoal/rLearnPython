"""
COIN		VALUE	WEIGHT			NUM PER WRAPPER
Penny: 		.01		2.500 grams		50
Nickel:		.05		5.000 grams		40
Dime:		.10		2.268 grams		50
Quarter:	.25		5.670 grams		40
"""

# IDEA: put above data into a list and loop thru it
from math import ceil

coin_types = [
['pennies', .01, 2.500, 50],
['nickels', .05, 5.000, 40],
['dimes', .10, 2.268, 50],
['quarters', .25, 5.670, 40]
]

bank = 0.0 
for coin, value, weight, roll in coin_types:
	coin_weight = float(raw_input("Enter weight of %s:" % coin))
	num_coins = ceil(coin_weight / weight)
	num_rolls = ceil(num_coins / roll)
	total_value = float(num_coins * value)
	bank += total_value
	print("You have %d %s totaling $%.2f. You will need %d rolls." % (num_coins, coin, total_value, num_rolls))
print("Your total is $%.2f" % bank)