#Mean, median, mod, etc
import sys

#find the sum of first N natural number

N = input("Enter the Number - ")
N = int(N)
i = sum = 0
while i <= N:
    sum += i
    i += 1
print(sum)

#find the square sum of first N natural number

N = input("Enter the Number - ")
N = int(N)
i = sum = sum_sq = 0
while i <= N:
    sq = i ** 2
    sum_sq += sq
    i += 1
print(sum_sq)

#find the ROOT MEAN SQUARE of first N natural number

N = input("Enter the number - ")
N = int(N)
i = sum = sum_sq = 0
while i <= N:
    sq = i ** 2
    sum_sq += sq
    i += 1
root_mean_sq = ((sum_sq / N) ** (1/2))
print(f"Root Mean Square of the data is {root_mean_sq}")


# find the MEAN of first N natural number

N = input("Enter the number - ")
N = int(N)
i = sum = sum_sq = 0
while i <= N:
    sum += i
    i += 1
mean = sum / N
print(f"Mean of the data is {mean}")

# Ask user for

X = []
while True:
    fnum = float(input("Enter the number"))
    X.append(fnum)
    que = input("Continue??")
    if que != "y" and que != "yes" and que != "YES" and que != "Yes" and que != "Y":
        break

print(X)
if len(X) == 0:
    print("Enter at least 1 number to find mean")
    sys.exit(-1)
sum = 0
for i in X:
    sum += i
print(sum)

mean = (sum / len(X))
print(f"The mean of the list is {mean}")

#Variance and starndard dev

X = []
while True:
    fnum = float(input("Enter the number"))
    X.append(fnum)
    que = input("Continue??")
    if que != "y" and que != "yes" and que != "YES" and que != "Yes" and que != "Y":
        break

print(X)
if len(X) == 0:
    print("Enter at least 1 number to find mean")
    sys.exit(-1)
sum = 0
for i in X:
    sum += i
print(sum)

mean = (sum / len(X))
print(f"The mean of the list is {mean}")

s = i = 0
while i < len(X):
    s += (X[i] - mean) ** 2
    i += 1

population_variance = s / len(X)
standard_deviation = population_variance ** 0.5