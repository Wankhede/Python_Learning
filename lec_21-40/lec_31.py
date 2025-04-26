#Nested loops
print("Start of program")
i = 0
while i < 6:
    print(f"    i :- {i}")
    j = 0
    while j < i:
        print(f"j :- {j}")
        j += 1
    i += 1
print("End of program")

M = 12
i = 0
while i < int(M):
    print(f"  i = {i}")
    j = 0
    while j < M-6:
        print(f"j = {j}")
        j += 1
    i += 1
print(i * j)