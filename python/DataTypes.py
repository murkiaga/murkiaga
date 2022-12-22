text = "text" # string
number = -100 # integer
big_number = 100_000_000 # integer
decimal = 0.5 # float. Don't use if need to be accurate
complex = 8j # complex number

people = ["Mario", "Luigi"] # list
print("Mario" in people)

lotto_numbers = (1, 2, 3, 4, 5, 6) # tuple. Can not be changed after created.
numbers = range(1, 1000) # range. From 1 to 999

users = {'user1': 'mario123', 'user2': 'luigi2023'} # dictionary

unique_numbers = {1, 2, 2, 3, 3, 4} # set (only unique elements, not ordered)
unique_numbers2 = frozenset({1, 2, 2, 3, 3, 4}) #frozenset. Can't be edited

is_connected = True # boolean

is_empty = None # no value asociated