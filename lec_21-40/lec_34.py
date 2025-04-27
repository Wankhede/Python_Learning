# mode and median standard deviation and variance
D = {}
print(D)
print(type(D))
D[1.2] = 1.2
print(D[1.2])
print(D)

X = [1.1, 2.2, 1.1, 4.5, 2.2, 6.7, 8.3, 1.1, 2.2, 4.5, 9.8, 0.12, 1.1]

count = {}

for i in X:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print(count)
P = {1.1: 1}
print(P)
P["a"] = 36
print(P)
P[4.2] = 3

if "a" in P.keys():
    print("Present")
else:
    print("Absent")

P[1.1] = 1.111111
print(P)

print(P['a'] + 4)
print(P[4.2] + 37)
P[4.2] = P[4.2] + 1
print(P[4.2])
print(P)

del P['a']
print(P)
print(dir(dict))

D = {1.1: 2, 4.5: 5, 'a': 10, 7.8: 5}

for x in D:
    if 1.1 in D.keys():
        print("Present")
