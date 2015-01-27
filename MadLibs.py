"""
Goal:
Create a Mad Libs style game, where the program asks the user for certain types of words,
and then prints out a story with the words that the user inputted. The story doesn't have
to be too long, but it should have some sort of story line.

Subgoals:
If the user has to put in a name, change the first letter to a capital letter.
Change the word "a" to "an" when the next word in the sentence begins with a vowel.

"""

"""
Doug is a happy guy who likes to eat pancakes. He has a red pet aardvark named Gimpy
that eats peanut butter. 
"""

name1 = raw_input("Enter name: ")
adj1 = raw_input("Enter adjective: ")
food1 = raw_input("Enter food: ")
adj2 = raw_input("Enter adjective: ")
pet1 = raw_input("Enter pet: ")
name2 = raw_input("Enter name: ")
food2 = raw_input("Enter food: ")

print("%s is a %s guy who likes to eat %s." % (name1, adj1, food1)) 
print("He has a %s pet %s named %s that eats %s." % (adj2, pet1, name2, food2))
