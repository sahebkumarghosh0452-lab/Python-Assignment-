# Q.1
import sys
sys.stdout.write("Hello World")

#Output 
#Hello World

# Q.2
num = list(map(float, input("Enter numbers separated by space: ").split()))
t = 0
c = 0
for n in num:
    t += n
    c += 1
avg = t / c 
print("Average:", avg)

#Output 
# Enter numbers separated by space: 10 20 30
# Average: 20.0


#Q.3
n = int(input("Enter number of terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

#Output 
# Enter number of terms: 5
# 0 1 1 2 3

#Q.4

n = int(input("Enter N: "))
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#Output 
# Enter N: 5
# 1
# 2
# Fizz
# 4
# Buzz

#Q.5

num = list(map(float, input("Enter numbers: ").split()))
if len(num) == 0:
    print("The list is empty")
    exit()
n = len(num)
#Mean
t = 0
for num in num:
    t += num

mean = t / n

#Median
# Sort the list
num.sort()

if n % 2 == 1:
    # Odd number of elements
    median = num[n // 2]
else:
    # Even number of elements
    m1 = num[(n // 2) - 1]
    m2 = num[n // 2]
    median = (m1 + m2) / 2

#Mode
f = {}
for n in num:
    if n in f:
        f[n] += 1
    else:
        f[n] = 1
mc = 0
for c in f.values():
    if c > mc:
        mc = c
modes = []
for i in f:
    if f[i] == mc and mc > 1:
        modes.append(i)

print("Sorted Numbers:", num)
print("Mean:", mean)
print("Median:", median)

if len(modes) == 0:
    print("Mode: No mode (all values occur once)")
elif len(modes) == 1:
    print("Mode:", modes[0])
else:
    print("Modes (multiple):", modes)

#Output
# Enter numbers: 1 2 2 4 3 
# Sorted Numbers: [1.0, 2.0, 2.0, 3.0, 4.0]
# Mean: 2.4
# Median: 2.0
# Mode: 2.0

#Q.6

l=eval(input("Enter the list"))
n=len(l)
s=0
d=0
for i in l:
    s=s+i
m= s/n
for j in l:
  d=d+((m-j)**2)
sd=(d/n)**0.5
print("Standard Deviation:",sd)

#Output 
# Enter the list [2,4,6,8]
# Standard Deviation: 2.23606797749979

#Q.7
A=[]
B=[]
r=int(input("Enter the no. of rows"))
c=int(input("Enter the no. of columns"))
print("Enter the elements of first matrix")
for i in range(r):
    A.append([])
    for j in range(c):
      x=int(input("Enter the element of row"))
      A[i].append(x)
print("Enter the elements of second matrix")
for k in range(r):
    B.append([])
    for l in range(c):
      y=int(input("Enter the element of row"))
      B[k].append(y)

if len(A) != len(B) or len(A[0]) != len(B[0]):
    print("Matrix dimensions do not match")
else:
    C = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        C.append(row)
print("Resultant Matrix:")
for row in C:
        print(row)

#Output 
# Enter the no. of rows: 2
# Enter the no. of columns: 2
# Enter the elements of first matrix:
# 1
# 2
# 3
# 4
# Enter the elements of second matrix:
# 5
# 6
# 7
# 8
# Resultant Matrix:
# [6, 8]
# [10, 12]

#Q.8
actual = list(map(float, input("Enter actual values: ").split()))
predicted = list(map(float, input("Enter predicted values: ").split()))

if len(actual) == 0 or len(predicted) == 0:
    print(" Input lists must not be empty.")
    exit()

if len(actual) != len(predicted):
    print("Actual and predicted lists must be of equal length.")
    exit()

n = len(actual)
aes = 0
sqesum = 0

for i in range(n):
    e = actual[i] - predicted[i]
    aes += abs(e)
    sqesum += e * e

mae = aes / n
mse = sqesum / n

print("Number of observations:", n)
print("Mean Absolute Error (MAE):", mae)
print("Mean Squared Error (MSE):", mse)

#Output 
# Enter actual values: 10 20 30
# Enter predicted values: 12 18 33
# Number of observations: 3
# Mean Absolute Error (MAE): 2.3333333333333335
# Mean Squared Error (MSE): 5.666666666666667


#Q.9

m = eval(input("Enter square matrix: "))
n = len(m)

if any(len(r) != n for r in m):
    print("Not a square matrix")
    exit()

if n == 2:
    det = m[0][0]*m[1][1] - m[0][1]*m[1][0]

elif n == 3:
    det = (
        m[0][0]*(m[1][1]*m[2][2] - m[1][2]*m[2][1]) -
        m[0][1]*(m[1][0]*m[2][2] - m[1][2]*m[2][0]) +
        m[0][2]*(m[1][0]*m[2][1] - m[1][1]*m[2][0])
    )
else:
    print("Only 2x2 or 3x3 matrices supported")
    exit()

print("Determinant:", det)

#Output 
# Enter square matrix: [[1,2,3],[4,5,6],[7,8,9]]
# Determinant: 0