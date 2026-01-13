# 23-27 import, from, as, class, del

import math
print(math.sqrt(16))

from math import pi
print(pi)

import math as m
print(m.sqrt(25))

class Student:
    def greet(self):
        print("Hello")

s = Student()
s.greet()

a = 10
del a
