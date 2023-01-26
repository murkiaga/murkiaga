#can't have duplicated elements in a set
#they are unordered. Each time printing, there will have diferent order
#can't change (modify) items in a set

items: set ={'apple', 'banana', 10, True}
print(items)
print(len(items))

items.add('orange') #add 1 item
items.update(['carrot', 15]) #add multiple items

items.remove('banana') #error if does not exit
items.discard('baaa') #try to remove. No error.

print(items)

items2: set = {'apple', 'kiwi'}

new_set = items.union(items2) #union of 2 sets
new_set2 = items | items2 #conbine 2 sets

items.clear() #clear set.

new_set3: set = {'carrot', 15, 19}
print(new_set)

new_set.intersection_update(new_set3) #only items on both sets
print(new_set) # {'carrot', 15}

new_set4 = items2.symmetric_difference(new_set3) #return only items in 1 set
new_set2.symmetric_difference_update(new_set3) #update. only items in 1 set
print(new_set2)