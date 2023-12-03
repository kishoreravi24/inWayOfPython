#!/usr/bin/python3
import sys
x = int(sys.argv[1])

def fib(limit):
    a,b = 0,1
    while a<x:
        print(a,end="  ")
        a,b = b,a+b
    print()

fib(x)

