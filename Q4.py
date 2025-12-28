# Q.4
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
#Input 
Enter N: 5
#Output 
1
2
Fizz
4
Buzz
