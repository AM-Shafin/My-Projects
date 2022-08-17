#Print the sum of all numbers in range of 1 to 100 that are divisible by 5.

#---------Method 1------
result = 0
for num in range(101):
    if num%5 == 0:
        print(num)
        result += num
print("Sum is:", result)

print("\n\n\t\tMethods #2\n\n")
#---------Method 2------
result = 0
for num in range(5, 101, 5):
    print(num)
    result += num
print("Sum is:",result)
