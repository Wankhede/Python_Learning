#Looping

a = 5
print(a)

# List stores the address of other data types in it

l1 = [10,20,30,40,50]
i = 0
while i < len(l1)  :
    print(i, l1[i])
    i+=1

l2 = "My name is swapnil"
l2 = l2.replace(" ", "")
j = 0
while j < len(l2):
    print(l2[j])
    j+=1
for i in l2.split():
    print(i)