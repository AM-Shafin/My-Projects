#A python program that checks if input is positive or negative value
import sys

n = input("Please insert a number: ")
n = float(n)
if (n >= 0):
    print("Input is Positive value")
else:
    print("Input is Negative value")