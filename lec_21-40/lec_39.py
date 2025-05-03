L1 = list(range(10,130,10))
print(L1)

print(L1[5:1:-1])

print(L1[:5:1])

print(L1[:8:2])
print()
print(f"Here= {L1[:6:-2]}")
print(L1[2::3])
print(L1[6::-1])

print(L1[2::3])
print(L1[::])
print(L1[:])

for x in L1[:5]:
    print(x, end=" ")
print()
#Get the list of only the odd number indices

print(L1[1::2])

#Get the list of only the even number indices

print(L1[::2])

print()
for i in range(len(L1)):
    if i % 2 != 0:
        print(i, L1[i])

print(L1[0:10:][::-1])
print(L1[-5::])
print(L1)
print(L1[6:1:-1])