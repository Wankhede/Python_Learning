#List data type in depth

from sys import getrefcount


L1 = [1,2,3,4,55,67,8,9]
print(L1, type(L1), id(L1), len(L1), getrefcount(L1))

#Operators available for list 
L2 = ["a","b","c","d","e"]
L3 = L1 + L2 #[1,2,3,4,55,67,8,9,"a","b","c","d","e"]
print(L3) #concatenated version , L1 and L2 remains unaffected

L4 = L1 + L1
print(L4)
L5 = L1 * 2
print(f"This is L5 {L5}")

print(L1[0])

#Iterating through list using while loop

i = 0
while i < len(L1):
    print(L1[i], end=" ")
    i += 1
print()
#Iterating through list using for loop
for i in L1:
    print(i, end=" ")
print()
#Iterating through list using for loop with index
for i in range(len(L1)):
    print(L1[i], end=" ")

print()

#Move all the zero to left or right of without disrupting the sequence
L1 = [1,2,0,3,4,0,55,0,67,8,0,9]
L4 = []
count = 0
for i in L1:
    if i != 0:
        L4.append(i)
    else:
        count += 1

print(L4)
print(count)
print(count * [0] + L4 )
print(L4 + count * [0] )

r = range(5, 10)
print(r, type(r), dir(r))
for i in r:
    print(i, end=" ")
print()
p = list(range(101))
print(p, type(p), dir(p))
print(len(r))

L1 = list(range(1,10))
print(L1)

for i in L1:
    print(i, end=" ")

print()

for ii in range(-1,-20,-1):
    print(ii, end=" ")


# List slicing

P1 = L1[1:2]
print(P1)
P1 = L1[1:5]
print(P1)
P1 = L1[4:8]
print(P1)
P1 = L1[4:-2]
print(P1)
P1 = L1[-4:-1]
print(P1)
P1 = L1[::-1]
print(P1)


for x in L1[5:9]:
    print(x, end=" ")

print()

#use enumeration to index the set or list or dictionary
for (ind, val) in enumerate(L1[:5]):
    print(ind, val, end=" | ")

ss = {1,2,3,4,5,5,6,78,9}
#this will give typeerror set is not subscritable
# for i in ss:
#     print(ss[i])
print()
#To overcome this , we use enumerate to index the containers
for k,v in enumerate(ss):
    print(k,  v, end=" | ")
    
U1 = list(range(10,110,10))
print(U1)
print(U1[2:6])

# The above syntax used is 
# List["start_index": "end_index" - 1] 
# without changing the actual list , this is called slicing

#Building a list L[i:j] wihtout using the slicing

L1 = list(range(1,10))
print(L1)
L2 = []
i = 0
while i < len(L1):
    if i > 3 and i < 8:
        L2.append(L1[i])
    i += 1
print(L2)

