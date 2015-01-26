def triple():
	sides = []				
	for i in range(1, 4):
		print("Enter length of side %d: ") % i
		user_input = raw_input()
		sides.append(int(user_input))

	sides.sort()		# moves the hypotenuse t0 sides[2]
	if sides[0] * sides[0] + sides[1] * sides[1] == sides[2]*sides[2]:
		print("Yes, it is a Pythagorean triple.")
	else:
		print("No, it is not a Pythagorean triple.")

	choice = raw_input("Try again? y/n ")
	if choice == 'y':
		triple()

triple()



