#!/usr/bin/python3
matrix = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
    ]

for i in matrix:
    for j in i:
        print(j,end='  ')
    print()

transposed=[]
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)

