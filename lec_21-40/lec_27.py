# Let L be a non-empty list of integers. Develop an algorithm to print all even numbers
# in the list

for i in range(100):
    if i % 2 == 0:
        print(i)
    else:
    # if i % 2 != 0:
        print("Duhhh!!!")


# Let L be a non-empty list of integers. Develop an algorithm for finding out the min element
# in the list.

L = [-1,2,10,20,30,40,50,-8]
L2 = []
L3 = []
mini = L[0]
for i in L:
    if i < mini:
        mini = i
print(f"hiiii {mini}")

# Iterate through the list to find pairs whose sum equals 10
L = [-1,2,3,7,10,20,30,40,50,1,8]
L2 = []

for i in L:
    for j in L:
        if i + j == 10:
            L2.append((i,j))
print(L2)



