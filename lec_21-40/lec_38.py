#slicing in depth

L = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

print(L[2:10:2])
print(L[1:7:3])
print(f"This is testing - {L[3:11:3]}")
print(L[1:4:7])
print(L[4:4:2])
print(L[9:2:-2])
print(L[9:2:-5])

print(L[9:2:-2])


L = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
print(L[3:1:-1])
print(L[-3:-7:-1])
print(L[10:-1:-1])