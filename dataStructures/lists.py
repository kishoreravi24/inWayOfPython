#!/usr/bin/python3
#append - add an item to end of the list
#extend - append all the item from the iterables
#insert - insert a value with the index
#remove - remove the first element from the list whose value is equal to given input
#pop - removes the last item
#clear - removes all the items from the list
#index - return the index by passing the value
#count - return the number of times x appears in the list
#sort - sort the items of the list in place
#reverse - reverse the elements of the list in the place
#copy - return the shallow copy of the list

letters = ['a','b','c']
letters.append('d')
print(letters)

additional_letters = ['e','f']
letters.extend(additional_letters)
print(letters)

letters.insert(5,'g')
print(letters)

letters.remove('e')
print(letters)

letters.pop()
print(letters)

letters.clear()
print(letters)

letters = ['a','b','c']
print(letters.index('b'))

letters.append('c')
print(letters.count('c'))

letters.clear()
letters = ['b','c','a']
letters.sort()
print(letters)

letters.reverse()
print(letters)

copy_letters = letters.copy()
print(copy_letters)

#EOF

