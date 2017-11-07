#!/usr/bin/python

#This script will print the factorial of a given number

print ("Enter a number : ")
num=input()
factorial=1

if num < 0 :
	print ("Factorial dosenot exsist for negative numbers: ")
elif num == 0:
	print ("Factorial of zero is one")
else:
	for i in range(1,num+1):
		factorial=factorial*i
	print("Factorial of ",num,"is",factorial)

	
