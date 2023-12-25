# lambda argument:expression
y=lambda x:x+2
print(y(2))

l=lambda x,y:x+y
print(l(2,3))

# lambda and map,filter
# filter() is used to select specific elements based on a condition, while map() is used to transform elements by applying a function to each element in an iterable.

# lambda and map
iter1=[1,2,3]
iter2=[4,5,6]

updated_map=map(lambda x,y:x*y,iter1,iter2)
print(list(updated_map))

# lambda and filter
data_list = range(-5,5)
greater_than_zero = filter(lambda x:x>0, data_list)
print(list(greater_than_zero))


