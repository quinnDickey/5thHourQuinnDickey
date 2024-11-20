#Name:Quinn Dickey
#Class: 5th Hour
#Assignment: HW14
import math
from math import factorial

#1. Create a variable that asks the user for an integer and an empty intger variable.
num = int(input("pick a number"))

factorial = 1
i = 1
#3. Use the loop to find the factorial of that number. A factorial of a number is that number multiplied
#by every number before it until you reach 1.
#For example: 5! is 5 x 4 x 3 x 2 x 1 = 120


while i <= num:
	factorial = factorial * i
	i = i + 1



#4. Print the factorial.
print("factorial of ", num, " is ", factorial)