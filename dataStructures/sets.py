#!/usr/bin/python3
# set is a unordered collection with no duplicates
baskets = {'apple', 'apple','orange','pear'}
print(baskets)
print('apple' in baskets)
print('meow' in baskets)

a = set('hello')
b = set('world')
print(a)
print(b)

print(a-b) #letters in a but not in b
print(a|b) #letters in a or b or both
print(a&b) #letters in both a and b
print(a^b) #letters in a or b but not both

