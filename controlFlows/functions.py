#!/usr/bin/python3

def fib(n):
    """print a fibonacci series up to n."""
    a,b = 0,1
    while a<n:
        print(a,end='  ')
        a,b = b, a+b
    print()

fib(20)

# Default argumented value
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y','ye','yes'):
            print('yes selected')
            return True
        if ok in ('n','no','none'):
            print('no selected')
        retries = retries - 1
        if retries<0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok('Please enter yes or no:')

#Positional args
def positional_fun(age,name):
    print(f"Hi, {name}! you are {age} years old.")
positional_fun(10,"bob")

#keyword args
def keyword_fun(*args):
    for i in args:
        print(i)
keyword_fun(range(1,5))

#arbitary args
def arbitary_fun(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
arbitary_fun(name="bob",age=10,place="Tyson,virginia")

# map function

def square(x):
    return x ** 2
numbers_s = [1,2,3,4,5]
# map(function,iterable)
squared_numbers = list(map(square,numbers_s))
print(squared_numbers)

#lambda expressions
# small anonymous function created with the lambda keyword
def make_increment(n):
    return lambda x:x+n
f = make_increment(42)
print(f(0))
print(f(1))

add = lambda x,y:x+y
print(add(3,5))

numbers = [1,2,3,4,5]
# map(function i.e lambda , numbers i.e iterables) numbers.items() passed to x and return with the square root with 2 and add it in the list 
squared_numbers = list(map(lambda x:x ** 2, numbers))
print(squared_numbers)
