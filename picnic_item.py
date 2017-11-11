#!/usr/bin/python

#Given a name this script will tell the items to be brought by the person

items = {'apples':2, 'orange':4}

print 'so select item whose number you want'

for key in items.keys():
	print key
item = raw_input()
#print items[item], ' number of ' + item
print 'i am getting ' + str(items.get(item,0)) + ' number of ' + item

