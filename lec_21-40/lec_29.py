#Repeatethon
from sys import getrefcount
from time import sleep


print("Hello world")
print("Hello world")
print("Hello world")
print("Hello world")

a = 1.2
b = 2
c = True
print(b, type(b), getrefcount(b))
print(a, type(a), getrefcount(a))
print(c, type(c), getrefcount(c))
d = a
print(d, type(a), getrefcount(a))
print(b, type(b), getrefcount(b))

n = 10
print(n, type(n), getrefcount(n), id(n), ord("n"))
print(n, type(n), getrefcount(n), id(n), ord("n"))
m = n
print(m, type(m), getrefcount(m), id(m), ord("m"))
print(m, type(m), getrefcount(m), id(m), ord("m"))
o = m
print(o, type(o), getrefcount(o), id(o), ord("o"))

