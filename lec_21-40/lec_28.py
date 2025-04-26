
#String Slicing

text1 = "Thisisfirstmonth"
print(text1[6:-5])  #first
print(text1[:6])    #Thisis
print(text1[3:9])   #isfir
print(text1[::3])   #Tsfsoh
print(text1[:3:])   #Thi

text = "programming"
print(text[0:4]) #Prog
print(text[:6]) #progra
print(text[4:]) #ramming
print(text[3:7]) #gram
print(text[:len(text)-6]) #progr
print(text[-3:]) #ing
print(text[::3]) #pgmn

text1 = "Thisisfifthmonth"
d = {"first":"jan","second":"february","third":"march","forth":"april","fifth":"may","sixth":"june"}
print(dir(d))

match1 = text1[6:-5]
# if match1 in d1:
#     match1 = d[d1]
replacement = d.get(match1)  # Replace if found, else keep original
print(f"Thisis{replacement}month")

L = [2,5,77,94,3,11,1,100]
# m = next(iter(L))
m = L[0]
for x in L:
    if x < m:
        m = x
print(m)
N = 101
k = 2
upper_bound = int(N**0.5)
print(upper_bound)
while k <= upper_bound:
    if N % k == 0:
        print(N,k, "is not a prime number")
        break
    k = k + 1

if k == upper_bound+1:
    print(N,k, "is a prime number")


N = input("Enter the size of the list")
L = []
i = 0
while i < int(N):
    n = input("Enter the number in list")
    if n == "" or n == str:
        exit()
    else:
        L.append(int(n))
    i += 1
print(f"The whole list is {L}")

pos_num = []
neg_num = []
zero = []

for i in L:
    if i > 0:
        pos_num.append(i)
    elif i < 0:
        neg_num.append(i)
    else:
        zero.append(i)

print(f"Positive number - {pos_num}")
print(f"Negative number - {neg_num}")
print(f"zero            - {zero}")
