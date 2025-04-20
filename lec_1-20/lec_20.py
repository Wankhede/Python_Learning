
s = "ABC"
T = (100, 200, 300, 400)
L = [True, 100, 1.1, 3.8, False]
D = {'a' : 1.1, 'b' : 3.8, 3.11 : 8080}
S = {-1, -2, -3}

print(type(s))
print(type(T))
print(type(L))
print(type(D))
print(type(S))

print(s[0])
print(T[0])
print(L[0])
print(D['a'], D["a"])
print(S)


print(type(s[0]))
print(type(T[0]))
print(type(L[0]))
print(type(L[1]))
print(type(L[2]))
print(type(D['a']), type(D["a"]))
print("======================================")
i =0
while i < 5:
    print(i)
    i += 1

i =0
while i < 5:
    print(i, L[i], type(L[i]))
    i += 1


i =0
while i < 5:
    print("=======================")
    print(f"index:  {i}")
    print(f"Value:  {L[i]}")
    print(f"Type :  {type(L[i])}")
    print(f"id   :  {id(L[i])}")
    print("=======================")
    i += 1

D = {'a' : 1.1, 'b' : 3.8, 3.11 : 8080}

i = 0
while i < len(D):
    print("=======================")
    keys = list(D.keys())
    key = keys[i]
    print(f"Index : {i}")
    print(f"Value : {D[key]}")
    print(f"Type  : {type(D[key])}")
    print(f"id    : {id(D[key])}")
    print("=======================")
    i += 1
print("===================================================")
print(D.keys())

for x in D.keys():
    print(x, D[x])

L = [10, 20, [300, 400, 500], 30, 40]
print(L[0])
print(L[1])
print(L[2])
print(type(L[0]))
print(type(L[2]))

print(L[2][0])
print(L[2][1])
print(L[2][2])

L = [10, 20, (100, 200, 300), {'a':-10, 'b':-20}, 30, 40, [True, False], 1000]
print(L[0], type(L[0])) #10
print(L[2], L[2][1] ,  type(L[2]), type(L[2][1]))   #(100,200,300) 200
print(L[3], type(L[3]), L[3]['a'] , type(L[3]['a']))    #{'a':-10, 'b':-20} -10
print(L[6][0], type(L[6][0]))   #True
print(L[7]) #1000