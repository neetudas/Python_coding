#!/usr/bin/python

#This script will check if an entered pet name is present in the list

petNames = ['Luck','Lucy','Jenny']
petNameis = petNames
def toLower(i):
	return i.lower()
petNames=map(toLower,petNames)
print 'Enter a pet name'
name  = raw_input()
#name = name.lower()
if name.lower() in petNames:
	print name + 'Is a pet name'
else:
	print 'Pet '+ name + 'is not a pet name'
