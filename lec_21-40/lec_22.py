#List

L = [True, 10, 3.14, 'A']

print(type(L[0]))   #Boolean
print(L[2]) #3.14
print(L[3], type(L[3])) # A string

L = [[100, 200, 300], [400, 500, 600], [700, 800, 900]]
print(L[0]) #[100, 200, 300]
print(L[0][0] ,type(L[0]))  #100    list
print(L[1][1])  #500
print(L[2][2])  #900

#Tuple
T = ([True, 10, ["xyz", "pqr"]], 600, True, {'a':[100, 200], 'b' : (1000, 2000)}, {1, 2, 3})

print(len(T))   #5
print(T[0]) #[True, 10, ["xyz", "pqr"]]
print(T[2]) #True
print(T[4]) #{1, 2, 3}
print(T[0][0], T[0][2][0])  #True, xyz
print(T[3]["a"])    #[100, 200]
print(T[3]["a"][1]) #200
print(T[3]["b"][1]) #2000
print(T[4]) #{1, 2, 3}
print(T[0][2][0][0])    #x

i = 0
while i < len(T[0][2][0]):
    print(T[0][2][0][i])    #100, 200
    i += 1

print("lllll")

j = 0
t1 = list(T[3].keys())
while j < len(T[3]):
    t2 = t1[j]
    print(T[3][t2]) #1000, 2000
    j += 1

k = 0
while k < len(T[0][2][1]):
    print(T[0][2][0][k])    #x y z
    k += 1

k = 0
while k < len(T[0][2]):
    print(T[0][2][k])   #x y z
    k += 1



L = [(['ab', 'xyzqzy', {(100, 200) : 1000, 'xyz': {305, 605}}, 10, True], 100, 200), [114, 34, 118, 14], "Hey"]

print(L[0])
print(L[0][0])
print(L[0][2])
print(L[0][0][2])
print(L[0][0][2]["xyz"])
print(L[1][1])
print(L[0][2])
print("====")
print(L[2])
print(L[2][0],L[2][1],L[2][2])
print(L[0][0][1][0])
print(L[0][0][1][1])
print("---------")
print(L[0][0][4])
if type(L[0][0][4]) == bool:
    print("Boolean")
if type(L[0][0][2]) == dict:
    print("Inside")
    if type(L[2][0]) == tuple:
        print("Again inside")
    elif type(L[2][0]) == str:
        print("Hello Agaoin")

x = 0
while x < len(L[2]):
    print(L[2][x])
    x += 1

x = 0
while x < len(L):
    print(L[x])
    x += 1


x = 0
while x < len(L[1]):
    print(L[1][x])
    x += 1

x = 0
l2 = list(L[0][0][2].keys())
print(l2)
print("==================")
while x < len(L[0][0][2]):
    l1 = l2[x]
    print(L[0][0][2][l1])
    x += 1

