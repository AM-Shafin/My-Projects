number1 = input("Please type an integer and press enter: ")
number2 = input("Please type another integer and press enter: ")

print("number1 + number2 =", number1+number2)
#Input:23 and 9
#Output: 239. 
# input() function always return string. that's why number1 and number2 are string variable
#changing variables to int type
number1 = int(number1)
number2 = int(number2)
print("number1 + number2 =", number1+number2) 
#now 23 + 9 = 32
