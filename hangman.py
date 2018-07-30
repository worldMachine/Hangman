import random 

line = open("dictionary.txt").read() 

words = line.split()
myWord = random.choice(words)
wordChars = list(myWord)
numOfChars = len(wordChars)

#print(myWord)

i = numOfChars
strikes = 0
foundLetter = 0
board = ["_ "] * numOfChars
lettersGuessed = [""]

def printPrompt():
	print (" ")
	for el in board:
		print (el, end = " ")
	print(" ")
	print(" ")
	print ("Letters guessed: ")
	for g in lettersGuessed:
		print (g, " ", end = " ")
	print (" ")
	print (" ")
	print ("Strikes: ", strikes, "/ 6")
	print (" ")




#letter = input('Welcome to Hangman! I have chosen  a word. Choose your first letter: ')
print ('Welcome to Hangman! I have chosen  a word.')

for el in board:
		print (el, end = " ")
print(" ")
print(" ")
print ("Strikes: ", strikes, "/ 6")
print (" ")

while (strikes < 6 and foundLetter < numOfChars):
	letter = input("CHOOSE YOUR LETTER: ")
	if letter in lettersGuessed:
		print("You have already guessed this letter.")
		print(" ")
	else:
		lettersGuessed.append(letter)
		giveStrike = True
		i = 0
		print (" ")
		for let in wordChars:
			if  letter == let:
				print ("There is a(n) ", letter, " in this word at space ", i)
				print(" ")
				del board[i]
				board.insert(i, letter)
				giveStrike = False
				foundLetter = foundLetter + 1
			i = i + 1
		if giveStrike:
			strikes = strikes + 1

		printPrompt()
	
	

printPrompt()

if (strikes < 6):
	print ("Congratualation! You win Hangman!")
else:
	print ("Oooh, sorry! The word was: ", myWord)