sides = []
for i in range(1, 4):
	print("Enter length of side %d: ") % i
	user_input = raw_input()
	sides.append(user_input)

if(pow(int(sides[0]), 2) + pow(int(sides[1]), 2) == pow(int(sides[2]), 2)):
	print("Yes, it is a triple.")
else:
	print("No, it is not a triple.")


