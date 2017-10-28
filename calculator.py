#!/usr/bin/python

#This is a simple calculator to add subtract divide and multiply two give numbers

def add(x,y):
	return x+y
	print ('sum')
def sub(x,y):
	return x-y

def mul(x,y):
	return x*y

def div(x,y):
	return x/y

print "Select operation"
print '1: Add'
print '2:Sub'
print '3:mul'
print '4:div'
choice=input('Enter your choice 1/2/3/4: ')

num1=int(input('Enter your first number: '))
num2=int(input('Enter the second number: '))
if choice == 1:
	print "Sum of ", num1,num2, "=", add(num1,num2)
elif choice == 2:
	print("Subtarct of ", num1,num2, "=", sub(num1,num2))
elif choice == 3:
	print("Multipication of ", num1,num2, "=", mul(num1,num2))
elif choice == 4:
	print("division of ", num1,num2, "=", div(num1,num2))
else: 
	print("Enter the correct choice")
