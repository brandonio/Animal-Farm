name = input("Hey there! What is your name?\n")
thisRound = 0
x = ""

def getAnswer():
	answer = input("Which do you choose?\n").upper()
	while answer not in ["A", "B", "C", "D"]:
		print("You must choose 'A', 'B', 'C', or 'D'.")
		print("Please try again.")
		answer = input("Which do you choose?\n").upper()
	return answer

def pp(*args):
	for i in range(len(args)):
		print(chr(i+97).upper() + ": " + args[i] + ".") 
	return getAnswer()

def playAgain():
	global thisRound
	print("Don't worry! You can play again!")
	again = input("Do you want to?\n")
	if "Y" in again.upper():
		thisRound += 1
		tbg()
	else:
		exit()

def beginning():
	global name, thisRound
	print("OK " + name + ", let's get started.")
	print("There are four kinds of animals to choose from: ")
	answer = pp("The first one is a seal", "The second one is a cow", "The third one is a walrus", "The fourth one is a hamster")
	while answer != "B":
		print("Silly, " + name + "! This isn't that type of farm. Try again.")
		answer = pp("The first one is a seal", "The second one is a cow", "The third one is a walrus", "The fourth one is a hamster")
	print("Congratulations! You have a cow now!")
	thisRound += 1

def tbg():
	global thisRound, name, x
	print("Hey, " + str(name) + "! Welcome to your very own farm. This is round #" + str(thisRound) + ".")
	if thisRound == 1:
		print("From now on you'll automatically start with a cow.")
	print("What do you want to do with your cow?")
	x = pp("I love steak so I want to eat it", "I want it to breed so I can have more cows", "I want to enter it in a beauty pageant and win a prize", "I want to let it go")
	if x != "B":
		checkX()
	if x == "B":
		print("You have a lot of cows now. Good for you!")
		print("But what do you want to do with them?")
		x = pp("I'm still hungry so I want to eat them all", "I don't have enough cows. I want them to breed again", "I want them to win more prizes", "I want to let them all go")
		checkX()

def checkX():
	global x, name
	if x == "A":
		print("Oh no! It looks like you don't have any cows now!")
		playAgain()
	elif x == "B":
		print("OK, " + name + ". You have a lot of cows now...maybe even too many.")
		print("A few months later your cows take over the farm.")
		playAgain()
	elif x == "C":
		print("Congratulations! You now have a lot of money!")
		print("What do you want to do with your money?")
		calledC()
	elif x == "D":
		print("You are a good person!")
		print("But now you have no cows.")
		playAgain()

def calledC():
	global x
	x = pp("Use it to send my cows to another farm", "Buy even more cows", "Do nothing for the rest of my life", "Donate the money and my cows to charity")
	if x == "C":
		print("Well, you are done here, I guess. Good game!")
		playAgain()
	else:
		checkX()

beginning()

tbg()
