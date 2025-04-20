#Container Datatypes
from sys import getrefcount

s = "Hello World!!!"
L = [1,2,3,4,5,6]
T = (1,2,3,4,5,6)
D = {"a":"1","b":"2","c":"3"}
S = {-1,-3,-4}
print(type(s), s)
print(type(L), L)
print(type(T), T)
print(type(D), D)
print(type(S), S)

print(T.index(6))
print(T[0])

sT = ("a","v","b","r","e","e","fe")
print(sT, type(sT))

S1 = "abc"
S2 = "cba"

print(id(S1))
print(id(S2))
print(id(S1[0]))
print(id(S2[2]))
print(getrefcount(S1[0]))
print(getrefcount(S2[2]))

#Playing with dictionary
D1 = {"a":"1","b":"2","c":"3"}
D2 = {"c":"3","b":"2","a":"1"}

print(D1["a"])
print(D2["a"])
print(id(D1["a"]))
print(id(D2["a"]))
print(getrefcount(D1["a"]))
print(getrefcount(D2["a"]))
