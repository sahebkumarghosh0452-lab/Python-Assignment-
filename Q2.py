#Q.2 
num = list(map(float, input("Enter numbers: ").split()))
t = 0
c = 0
for n in num:
    t += n
    c += 1
avg = t/c
print("Average:", avg)
#Input 
Enter numbers: 10 20 30
#Output 
Average: 20.0
