
people: list[str] = ['Mario', 'Luigi', 'Peach', 'Toad'] 

print(len(people))
print(people)
print(people[-1]) # to get the last one
print(people[0:3]) # from index 0 to 2 (not included)
print(people[2:4]) # last 2 items

print('Luigi' in people) # is value 'Luigi' in the list?

people[0] = 'Malio'
people[0:2] = ['Mailo', 'Luiga']
print(people)


people.insert(2, '!!!') # insert value in index

people.append('Shy Guy') # add an element at the end
print(people)


people2 = ['Sonic', 'Tails']

new_list = people + people2
print(new_list)

new_list.remove('Mailo') # remove by value
new_list.pop() # remove last element
new_list.pop(2) # remove by index
print(new_list)

new_list.clear() # empty list []

people.reverse() # reverse order
people.sort() # sort list (in this case, alphabetical order)

print(people)
