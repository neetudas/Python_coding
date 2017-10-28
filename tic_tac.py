#!/usr/bin/python

#This is a tic tac toe game

theBoard = {'top-L':' ', 'top-M':' ', 'top-R':' ',
	    'mid-L':' ', 'mid-M':' ', 'mid-R':' ',
	    'low-L':' ', 'low-M':' ', 'low-R': ' '}

#Function will display the tic tac Board
def printBoard(board):
	print board['top-L'] + '|' + board['top-M'] + '|' + board['top-R']
	print '-+-+-'
	print board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R']
	print '-+-+-'
	print  board['low-L'] + '|' + board['low-M'] + '|' + board['low-R']

#Function will do a user entry validation
def validationForIncorrectInput(choice):
	while choice not in theBoard.keys():
		print 'Choice entered is incorrect, enter a choice as mentioned above'
		choice = str(raw_input())
	return choice
def validationForSamePlaceInput(choice):
	while theBoard[choice] != ' ':
		print 'Make a differnt choice as the place is already taken'
		choice = str(raw_input())
		if choice not in theBoard.keys():
			 choice = validationForIncorrectInput(choice)
	return choice

#Function will make an entry for first player choice
def firstPlayer():
	print 'Hi '+ player1 + ' enter your choice as mentioned above'
	choice = str(raw_input())
	#print choice
	choice = validationForIncorrectInput(choice)
#	print choice
	choice = validationForSamePlaceInput(choice)
	theBoard[choice] = '0'
	printBoard(theBoard)

#Function will make an entry for second player choice
def secondPlayer():
	print 'Hi '+ player2 + ' enter your choice as mentioned above'
        choice = str(raw_input())
	print choice
	choice = validationForIncorrectInput(choice)
	choice = validationForSamePlaceInput(choice)
        theBoard[choice] = 'X'
        printBoard(theBoard)


print 'This is a tic tact toe game, so lets begin'
print 'Enter the name of first player'
player1 = str(raw_input())
player1 = player1.lower()
print 'Enter the name of second player'
player2 = str(raw_input())
player2 = player2.lower()
print 'Totl choices are '
for keys in theBoard:
	print keys

printBoard(theBoard)
for i in range (1,10):
	if i%2 != 0 :
		firstPlayer()
	else:
		secondPlayer()
#printBoard(theBoard)
