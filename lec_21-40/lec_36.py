L1 = [10, 20, 30, 40, 50, 25]
print("Before:L1:", L1) 

tmp = L1[len(L1) - 1]
i = len(L1) - 2 
while i > -1 and tmp < L1[i]:
    L1[i + 1] = L1[i]
    i -= 1

L1[i+1] = tmp
print("After:L1:", L1)

L2 = [1,2,8,6,7,4]
print("Before:", L2)
i = len(L2) - 2
tmp = L2[len(L2) - 1]
while i > -1 and tmp < L2[i]:
    L2[i + 1] = L2[i]
    i -= 1
L2[i + 1] = tmp
print("After:", L2)

 

L = [1,2,8,6,7,4]
print("Before:", L)

tmp = L[len(L) - 1]
i = len(L) - 2
while i > -1 and L[i] >  tmp:
    L[i + 1] = L[i]
    i -= 1
L[i + 1] = tmp

print("Before:", L)

L = [ 9, 7, 5, 1, 2, 4]
j = 1
while j < len(L):
    tmp = L[j]
    i = j - 1
    while i > -1 and tmp < L[i]:
        L[i + 1] = L[i]
        i -= 1
    L[i + 1] = tmp
    j += 1
print(L)

#Proper sorting algorithm -> Insertion sort

L = [ 9, 7, 5, 1, 2, 4]
k = 1
while k < len(L):
    tmp = L[k]
    i = k - 1
    # print(f"k is - {k}, tmp- {tmp} ")
    while i > -1 and L[i] > tmp:
        L[i + 1] = L[i]
        # print(f"i is - {i}, tmp- {tmp}, L[i] - {L[i]}")
        i -= 1
    L[i + 1] = tmp
    k +=1
print(L)


N = int(input("Enter the lenght of the list - "))
i = 0
L = []
while i < N:
    a = int(input("Enter the elements - "))
    L.append(a)
    i += 1
print(L)

j = 1
while j < len(L):
    tmp = L[j]
    i = j - 1
    while i > -1 and L[i] > tmp:
        L[i + 1] = L[i]
        i -= 1
    L[i + 1] = tmp
    j += 1
print(L)


