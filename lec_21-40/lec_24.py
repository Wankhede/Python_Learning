from sys import getrefcount

s = "abc"
t = [(10,20,30)]
print(type(t))
print(type(t[0]))
t.append(30)
print(type(t[0]))
print(type(t[1]))
print(t)
l = [10,20,30]
m = 10
for ss in s:
    print(ord(ss))
    print(ss)
    print(id(ss))
    print(getrefcount(ss))

for ss in t:
    # print(ord(ss))
    print("tuple")
    print(ss)
    print(id(ss))
    print(getrefcount(ss))

for ss in l:
    # print(ord(ss))
    print("list")
    print(ss)
    print(id(ss))
    print(getrefcount(ss))

print(id(m))
print(getrefcount(m))
