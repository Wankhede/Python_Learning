# Nested Loops
L1 = []
L2 = []
L3 = []
L4 = []
L5 = []

i = 0
while i < 6:
    j = 0
    while j < i:
        print(f"{i} {j}")
        L1.append((i,j))
        j += 1
    i += 1
print("Next prog")
i = 0
while i < 6:
    j = 0
    while j <= i:
        print(i, j)
        L2.append((i,j))
        j += 1
    i += 1
print("Next prog")
i = 0
while i < 6:
    j = i
    while j < 6:
        print(i,j)
        L3.append((i,j))
        j += 1
    i += 1
print("Next prog")
i = 0
while i < 6:
    j = 0
    while j < 6:
        if i == j:
            print(i , j)
            L4.append((i, j))
        j += 1
    i += 1
print("Next prog")
i = 0
while i < 6:
    j = 0
    while j < 6:
        if i != j:
            print(i, j)
            L5.append((i, j))
        j += 1
    i += 1
print(L1)
print(L2)
print(L3)
print(L4)
print(L5)