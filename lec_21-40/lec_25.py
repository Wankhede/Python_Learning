#Starting coding from today
from datetime import time

#For loop demo
L = [100,200,300,400,500]
for x in L:
    print(x, type(x))

print("End of 1\n")
L = [True, 10, (100, 200), {'a':1.1, 'b':2.2}, 3.7, "hello"]
for x in L:
    print(x, type(x))

print("End of 2\n")

int1 = 20
try:
    for x in int1:
        print(x)
except TypeError as e :
    print(e)
#TyperError int is not interable

b = True
try:
    for c in b:
        print(c)
except TypeError as e:
    print(e)
#TyperError bool is not interable

f = "s"
for d in f:
    print(d)

ss = {"x","y","z"}
print(type(ss))
for f in ss:
    print(f, type(f))

#To get the key and values in dictionary when we dont know the key and value
d = {"a":1,"b":2,"c":3}
for x in d:
    print(x,d[x])
print("End of 3\n")

l1 = dir(list)
if "append" in l1:
    print("yes" , type(l1))
