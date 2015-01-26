"""
    Allow the user to enter their question
    Display an in progress message( i.e. "thinking")
    Create 20 responses, and show a random response
    Allow the user to ask another question or quit
	
	Bonus Using whatever module you like, add a gui. Your gui must have:
    A box for users to enter the question
    At least 4 buttons: Ask , clear(the text box), play again and quit(this must close the window)
"""
import random
import time
import sys

answer = ['yes','no','of course','no way','duh','hell yea','nope','hell no',
		  'not sure','ask again','no response','not gonna answer','why not']

def question():
	print("Ask a question, or type 'quit' to exit: ")
	user_input = raw_input()
	if user_input == 'quit':
		sys.exit(0)
	else:
		print("Thinking...")
		time.sleep(3)
		print(random.choice(answer))


question()

