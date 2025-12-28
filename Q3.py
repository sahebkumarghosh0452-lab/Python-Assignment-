#Q.3
n=int(input("Enter the number :"))
x=0
y=1
for i in range(n):
  print(x,end=" ")
  c=x+y
  x=y
  y=c
#Output 
Enter the number :5
0 1 1 2 3
