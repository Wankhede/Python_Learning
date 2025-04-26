import sys

L = [10,20,30,40,50]

for x in L:
    print(x, type(x))

print("\n Stmt 2\n")
L = [(10, 20), (30, 40), True, 3, {'a':100, 'b':200}, (50, 60), 1.1]

for xx in L:
    print(xx, type(xx))
    if xx == 3:
        break

for i in range(0,10):
    print(i)
    if i == 4:
        break


# n = input("Enter")
# if len(n) == 0:
#     raise  ZeroDivisionError
#
print("Start of the program")
# raise TypeError

N = int(input("Enter the num of ele in list"))

if N < 0:
    print("0 element in list")
    sys.exit(-1)


L = []
i = 0
while i < N:
    L.append(int(input("Enter num :- ")))
    i += 1

print("Break Demo")

for x in L:
    print("Start of iteration")
    if x % 7 == 0:
        break
    print(x)
    print("End of iteration")

print("Continue Demo")

for x in L:
    print("Start of iteration")
    if x % 7 == 0:
        continue
    print(x)
    print("End of iteration")
print("End of program")

