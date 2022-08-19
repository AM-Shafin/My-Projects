#Write a function that takes a list in perimeter and returns average of the list

from curses.ascii import isdigit


def average(list):
    total = sum(list)
    return total/len(list)

list = [10, 2, 38, 23, 38, 23, 21]
print(average(list))

print("---------------------------------------\n\n\n")

#write a function that prints Multiplaction table of the number of it's perimeter. 
def namta(num):
    print("Multiplication table of", num)
    for i in range(1, 11):
        print(num,"X",i,"=",num*i)

num = int(input("Please enter a number for it's multiplication table: "))
namta(num)