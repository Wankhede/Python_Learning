from sys import getrefcount, base_prefix

a = 22
b = 4
list1 = [1,2,3,4,5,6,7,8,9,0]
print(getrefcount(a))
print(getrefcount(b))
print(id(a))
print(id(b))

print(a == b)
print(a != b)

print(type(a))
print(type(b))
print(type(list1))

c = a + b
print(c)

d = a - b
print(d)

#to get the quotient
e = a / b
print(e)
print(type(e))

#to get the integer value quotient
f = a // b
print(f)
print(type(f))

#to get the remainder only
g = a % b
print(g)
print(type(g))

#to get the power value that is the raise to value
h = a ** b
print(h)
print(type(h))

#Arbitarary precision mathematics
#In other prog language we can only store the integer value till
i = 2 ** 64 -1
print(i)

n1 = 82130948721309487102983470198234709182374098123470918237409812734098172340987123094871029384709183740981327409182734098123740981237409812374098172340981723409871234098712304987123098471209384719028347091283740918234709813274098123749081234710928347102938471092837412390847
n2 = 82130948721309487102983470198234709182374098123470918237409812734098172340987123094871029384709183740981327409182734098123740981237409812374098172340981723409871234098712304987123098471209384719028347091283740918234709813274098123749081234710928347102938471092837412390847923798237492873492837492873498374098327419083740918324709182374981023749012387409123874091328471903284
print(n1 + n2)
print("Sub")
print(n1 - n2)
print("mul")
print(n1 * n2)
print("power")
# print(n1 ** n2)
print("remainder")
print(n1 % n2)
print("Quotient")
print(n2 // n2)

#To generate ASCII code

s1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s2 = "abcdefghijklmnopqrstuvwxyz"
s3 = "1234567890"

for c in s1:
    print(ord(c), end=" ")
print()
for c in s2:
    print(ord(c), end=" ")
print()
for c in s3:
    print(ord(c), end=" ")
print()
s4 = zip(s1, s2)
d1 = dict(s4)
print(d1)

name = "Swapnil"
sum1 = 0
for s in name:
    sum1 = sum1 + ord(s)
    print(ord(s))
print(sum1)

print(ord(" "))
print(ord("\t"))
print(ord("\n"))
print(ord("."))

swapnil = 5.5
print(swapnil)
print(globals())