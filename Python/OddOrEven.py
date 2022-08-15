# A python program that takes a number and checks for odd or even number and print the result
num = input("Insert an integer number: ")
num = int(num)

if (num % 2) == 0:
    print(num, "is even number.")
else:
    print(num, "is odd number.")
