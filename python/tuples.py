# tuples can't be modificated one created

people: tuple = ('Mario', 'Luigi', 'Peach', 'Luigi', 'Shy Guy', 10) # parenthesis not required

print(type(people)) # <class 'tuple'>

people_list: list[str] = list(people)

print(people[0]) # same as lists

print('Luigi' in people)

# if you want to edit a tuple, first you must convert into list, and then reconvert into a tuple

print(people.count('Luigi')) # counts how many times value is in tuple

print(people.index('Luigi')) # return the first index of value

a, b, c, *d = people # unpack values into variables, the * variable will have all the rest values
print(a) # Mario
print(d) # ['Luigi', 'Shy Guy', 10]