#If statements
#Ask input
x = int(input("Please enter an integer:"))
if x<0:
    print("Negative number")
elif x==0:
    print("Zero")
elif x==1:
    print("1")
else:
    print("More")


#For statements
words = ['cat','dog','window']
for w in words:
    print(w,len(w))

# indexes or slices need to be in the brackets
del words[0]
print(words)

#Range function
for i in range(5):
    print(i)

a = list(range(5,10))
print(a)

# Range with addition of nums
b = list(range(0,10,3))
print(b)

c = sum(range(1,5))
print(c)

#Break statement
for n in range(2,10):
    for m in range(2,n):
        if n%x==0:
            print(n, 'equals',m,'*',n//m)
            break
        else:
            print(n,' is a prime number')

for num in range(2,10):
    if num%2 == 0:
        print("Found an even number ", num)
        break
    else:
        print("Found an odd number ", num)

# pass statement
for nums in range(1,3,2):
    if nums==1:
        pass
    else:
        print(nums, " printed correctly")

