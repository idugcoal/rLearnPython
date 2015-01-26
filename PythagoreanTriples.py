def triple():
	sides = []
	for i in range(1, 4):
		print("Enter length of side %d: ") % i
		user_input = raw_input()
		sides.append(int(user_input))

	if(sides[0]*sides[0] + sides[1]*sides[1] == sides[2]*sides[2]):
		print("Yes, it is a triple.")
	else:
		print("No, it is not a triple.")

	print("Try again? y/n")
	choice = raw_input()
	if choice == 'y':
		triple()

triple()



