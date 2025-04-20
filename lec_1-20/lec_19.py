
from sys import getsizeof


set_1 = {-1,-2.-3}
print(type(set_1))
print(set_1)

list1 = list(set_1)
print(list1)
list1.append(4)
print(list1)

print(getsizeof(list1))
n =10
print(getsizeof(n))
m = 29348203948203948209348029348023984023984023948203948203948203948230948230948230498
print(getsizeof(m))

t = (-12)
print(getsizeof(t))

s = "a"
print(getsizeof(s))

d = {1: 11, 2:22}
print(getsizeof(d))
print(d)

