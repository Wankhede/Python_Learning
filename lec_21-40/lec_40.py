
#Left shift of the list

import sys


L1 = [10,30,50,16,99,34,54,56,999]
tmp = L1[len(L1) - 1]
i = len(L1) - 2
print(L1)

while i > -1:
    L1[i + 1] = L1[i]
    i -= 1
L1[i + 1] = tmp
print(L1)

#Right shift of the list

L1 = [10,30,50,16,99,34,54,56,999]
print(L1)
tmp = L1[0]
i = 0

while i < len(L1) -1 :
    L1[i] = L1[i + 1]
    i += 1
L1[len(L1) - 1] = tmp
print(L1)

#Single element sort 

L2 = [1,2,8,6,7,4]
print("Before:", L2)
i = len(L2) - 2
tmp = L2[len(L2) - 1]
while i > -1 and tmp < L2[i]:
    L2[i + 1] = L2[i]
    i -=1
L2[i + 1] = tmp
print("After:", L2)

#insertion sort
L2 = [1,2,8,6,7,4]
j =1
while j < len(L2):
    i = j -1
    print(i , j)
    tmp = L2[j]
    while i > -1 and L2[i] > tmp:
        L2[i + 1] = L2[i]
        i -= 1
    L2[i + 1] = tmp
    j += 1
print(L2)

#insertion sort
L = [1,2,8,6,72,89,7,4,44,36,99]
j = 1
while j < len(L):
    i = j -1
    tmp = L[j]
    while i > -1 and L[i] > tmp:
        L[i + 1] = L[i]
        i -= 1
    L[i +1] = tmp
    j += 1
print(L)

L1 = [10, 20, 30, 40]
L2 = [40, 50, 60, 70, 80]
L3 = L1 + L2
print(L1, L2, L3)
L4 = L3 * 0
L5 = L3 * 2
print(L4)
print(L5)
i = 0
for i in range(len(L3)-1):
    print(i, L3[i])

print(dir(list))
print(dir(__builtins__))

L = [10, 20, 30, 40, 10, 20, 10, 60, 70, 10, -100]

print(L.count(10))
print(L.count(20))
print(L.count(60))
print(L.count(70))
print(L.index(10))
print(L.count(-120))
print(L.count(-100))
print(L.index(10, 1))
print(L.index(10, 5))
print(L.index(20, 2))

L1 = []
while True:
    x = input("Enter the no. in list - ")
    if len(x) > 0:
        L1.append(x)
    else:
        break
print(L1)
ask = input("Enter the no. you want to count in the list")
print(L1.count(ask))

ask_1 = input("Enter the index of the number you want to find")
print(L1.index(ask_1))

T1 = (-1.2,2.3,65)
L1.append(T1)

print(L1)
T2 = (-1.2,2.3,65)

L1.extend(T2)
print(L1)

T3 = ["abc", "bdc" , "fhi"]
L1.extend(T3)
print(L1)

L1.insert(1, 10000)
print(L1)

L1.insert(len(L1)-1, 5555)
print(L1)