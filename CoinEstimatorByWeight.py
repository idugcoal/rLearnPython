"""
COIN		VALUE	WEIGHT			NUM PER WRAPPER
Penny: 		.01		2.500 grams		50
Nickel:		.05		5.000 grams		40
Dime:		.10		2.268 grams		50
Quarter:	.25		5.670 grams		40
"""

# IDEA: put above data into a list and loop thru it

weight_pennies = int(raw_input("Weight of pennies: "))
weight_nickels = int(raw_input("Weight of nickels: "))
weight_dimes = int(raw_input("Weight of dimes: "))
weight_quarters = int(raw_input("Weight of quarters: "))

num_pennies = weight_pennies / 2.500
num_nickels = weight_nickels / 5.000
num_dimes = weight_dimes / 2.268
num_quarters = weight_quarters / 5.670
