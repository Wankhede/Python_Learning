
import sys


# def main():
#     print("Hello Visual studio world!")
#     sys.exit(0)

# main()

#Shift and rotate the list

L = [10, 20, 30, 40, 50]
print(L)
tmp = L[len(L) - 1]
i = len(L) - 2
while i > -1:
    L[i + 1] = L[i]
    i -= 1
L[i + 1] = tmp
print(L)

#Repeatethon 

print("Start")
L = [10, 20, 30, 40, 50]
tmp = L[len(L) - 1]
i = len(L) - 2
while i > -1:
    L[i + 1] = L[i]
    i -= 1
L[i+1] = tmp
print(L)
print("End")

print("Start")
L = [10, 20, 30, 40, 50]
tmp = L[len(L) - 1]
i = len(L) - 2
while i > -1:
    L[i + 1] = L[i]
    i -= 1
L[i + 1] = tmp
print(L)
print("End")

print("Start")
L = [10, 20, 30, 40, 50]
tmp = L[len(L) - 1]
i = len(L) - 2
while i > -1:
    L[i + 1] = L[i]
    i -= 1
L[i + 1]= tmp
print(L)
print("End")

print("Start")
L = [10, 20, 30, 40, 50]
tmp = L[len(L) -1]
i = len(L) -2
while i > -1:
    L[i + 1] = L[i]
    i -= 1
L[i + 1] = tmp
print(L)
print("End")

print("Start")
L = [10, 20, 30, 40, 50]
tmp = L[len(L) - 1]
i = len(L) - 2
while i > -1:
    L[i + 1] = L[i]
    i -= 1
L[i + 1] = tmp
print(L)
print("End")

L = [10, 20, 30, 40, 50]
print(L)
tmp = L[len(L) - 1]
while i > -1:
    L[i + 1] = L[i]
    i -= 1
L[i+1] = tmp
print(f"This is {L}")

L = [10, 20, 30, 40, 50]
last = L[-1]
for i in range(len(L) -1, 0, -1):
    L[i] = L[i - 1]
L[0] = last
print(L)

L = [10, 20, 30, 40, 50]
first = L[0]
for i in range(len(L) - 1):
    L[i] = L[i + 1]
L[len(L) - 1] = first
print(L)

L = [10, 20, 30, 40, 50]
first = L[0]
i = 0
while i < len(L)-1:
    L[i] = L[i + 1]
    i += 1
L[len(L) - 1] = first
print(L)



#Right shift the list by 1
L = [10, 20, 30, 40, 50, 60, 70, 80] # op = [80, 10, 20, 30, 40, 50, 60, 70]
tmp = L[len(L) -1]
i = len(L) -2
while i > -1:
    L[i + 1] = L[i]
    i -= 1
L[i + 1] = tmp
print(L)

#Left shift the list by 1
L = [10, 20, 30, 40, 50, 60, 70, 80] # op = [20, 30, 40, 50, 60, 70, 80, 10 ]
tmp = L[0]
i = 0
while i < len(L) - 1:
    L[i] = L[i + 1]
    i += 1
L[len(L) - 1] = tmp
print(L)

L = [50, 40, 65, 51, 30, 35, 20, 25, 40]
print(L)
# last_element = L[len(L) -1]
# second_last_element = L[len(L) -2]
i = len(L) - 2
tmp = L[len(L) - 1]
while i > -1 and tmp > L[i]:
    print(L[i])
    i -= 1
if i == -1:
    print(f"{tmp} is greatest element in list")
else:
    print(f"{L[i]} is first element in list")


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

