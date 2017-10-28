#!/usr/bin/python

#This script will the tell the items brought for the quest

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
items_total = 0
def displayInventory(inventory):
	print 'Inventory:'
	for i, j in inventory.items():
		print str(i) + ' ' + str(j)
		total = items_total + j
		return total
total = displayInventory(inventory)
print 'total items are ', total
	

	

