''' Accessing Values in Dictionary'''
# Declare a Dictionary
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# Accessing the dictionary with its key
print("dict['Age']: " , dict['Name'])
print("dict['Age']: ", dict['Age'])

''' Updating Dictionary'''
# Declare dictionary
dict = {'Name': 'Zara', 'Age': 7, 'Class':'First'}
dict['Age'] = 8; #update existing entry
dict['School'] = "DPS School"; #Add new entry
print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])

'''Delete Dictionary Elements'''
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
del dict['Name']; #remove entry with key 'Name'
dict.clear(); #remove all entries in dict
del dict ; #delete entire dictionary

print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])
