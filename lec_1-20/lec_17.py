#Prove that the square of all odd num is odd number

for i in range(0, 100):
    if i % 2 != 0:
        sq = i ** 2
        if sq % 2 != 0:
            print(str(i) + " " + str(sq) + " |", end=" ")
        else:
            print("Sorry you are wrong!!!")

#The above solution is true for a finite collection but for infinite collection no

#If you want to prove a certain property to be true for all the elements in a collection (esp an infinite collection)
#then you must prove that property to be true for an ARBITRARY element in the collection
#Print all the even number in the range 100 using while

print()

i = 0
while i <= 100:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1

print()
L1 = []
L1.append("10,20,30,40")
L1.append(20)
print(L1)
for i in range(len(L1[0])):
    print(i, L1[0][i])
print(L1[1])


# Take input from the user and ask the length of the list to print

s = input("Enter the lenght of the list")
ss = int(s)
if ss <= 0:
    print("Negative number nako re bhau")
else:
    L2 = []
    i = 1
    #for i in range(ss):
    while i <= ss:
        L2.append(i)
        i += 1
    print(L2)

# Now take a dynamic list

L3 = []
n = input("Enter the number elements to be added to the list :- ")
nn = int(n)
i = 0
while i < nn:
    d = input("Enter the number: -")
    dd = int(d)
    L3.append(dd)
    i += 1
print(L3)

# print a dynamically increasing list

L4 = []

while True:
    g = input("Enter the element in the list :- ")
    if len(g) > 0:
        L4.append(g)
    else:
        break
print(L4)

L5 = []
g = input("Enter the element in the list :- ")
while len(g) > 0:
    L5.append(g)
    g = input("Enter the element in the list :- ")
print(L5)