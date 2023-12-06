#!/usr/bin/python3
class myClass:
    def __init__(self,a,b):
        self.hello = a
        self.hi = b

x = myClass(10,"hello")
print(x.hello,x.hi)
del x

