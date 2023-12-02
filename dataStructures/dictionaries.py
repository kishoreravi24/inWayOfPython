#!/usr/bin/python3
tel = {'x':12,'y':24}
print(tel)

del tel['x']
print(tel)

tel['x']=12
print(tel)

tel['z']=1
sorted(tel)
print(tel)

print('x' in tel)
print('h' not in tel)

