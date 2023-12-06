#!/usr/bin/python3
class MyClass:
    def __init__(self):
        self._private_var = 10
    def get_private_var(self):
        return self._private_var
    def set_private_var(self,value):
        self._private_var = value

x = MyClass()
print(x.get_private_var())
x.set_private_var(20)
print(x.get_private_var())

