
users = {
    'user1': 'Mario123',
    'user2': 'Luigi123'
}

print(len(users))

user1 = users['user1'] #error if doesn't exist
user2 = users.get('user2') #None if doesn't exist
print(user1)

x = users.keys()
y = users.values()
print(x)

users['user1'] = 'Toad678' #update value of 'user1'

z = users.items() #distionary data type
z_list = list(users.items()) #as an array
print(z)
print(z_list[0])

users.update({'hello': 123}) # add new key:value
users.pop('user1') #remove
users.popitem() #remove last 
users.clear() #clear distionary

#nested dictionaries
users = {
    'user1': 'Mario123',
    'user2': 'Luigi123',
    'items': {
        'apple': 10,
        'banana': 20
    }
}
print(users['items']['apple'])
print(users.setdefault('xxx', 'There is no key!')) #Default feedback if key doesn't exist