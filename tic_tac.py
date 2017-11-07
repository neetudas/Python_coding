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
def isCorrectInput(choice):
	if( choice not in theBoard.keys() ):
		print "Enter correct input"
		return False
	return True

def isPositionFree(choice):
	if( theBoard[choice] != ' '):
		print "Enter Correct position"
		return False
	return True

#Function will make an entry for first player choice
def player(player, playerMark):
	print 'Hi ' + player + ' enter your choice as mentined above'
	choice = str(raw_input())
	while( not isCorrectInput(choice) or not  isPositionFree(choice) ):
		choice = str(raw_input())

	theBoard[choice] = playerMark
	printBoard(theBoard)

print 'This is a tic tact toe game, so lets begin'
print 'Enter the name of first player'
player1 = str(raw_input()).lower()
print 'Enter the name of second player'
player2 = str(raw_input()).lower()
print 'Totl choices are '
for keys in theBoard:
	print keys

printBoard(theBoard)
for i in range (1,10):
	if i%2 != 0 :
		player(player1, '0')
	else:
		player(player2, 'X')

#printBoard(theBoard)
