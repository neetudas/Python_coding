#!/usr/bin/python

#This script will tell you the number of occurence of a word in a letter

import pprint

print 'Enter a message'
message = raw_input()
#print 'Enter the letter whose occurenence you need'
#letter = raw_input() 
counter = {}
print 'letter counts is'
for i in message:
	counter.setdefault(i,0)
	counter[i]=counter[i]+1

pprint.pprint (counter)



