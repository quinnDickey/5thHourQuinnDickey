#Name:Quinn Dickey
#Class: 5th Hour
#Assignment: HW20

#1. Create a try catch that tries to print variable x (which has no value), but prints "Hello World!" instead.
try:
    print(x)
except:
    print("hello world")
#2. Create a try catch that tries to divide 100 by whatever number the user inputs, but prints an exception for Divide By Zero errors.
try:
    z=int(input("give a number"))
    print(100/z)
except ZeroDivisionError:
    print("error division by zero")
#3. Create a variable that asks the user for a number. If the user input is not an integer, prints an exception for Value errors.
try:
    int(input("give a number"))
except ValueError:
    print("error non-number")

#4. Create a while loop that counts down from 5 to 0, but raises an exception when it counts below zero.
try:
    i=5
    while i>-1:
       print(i)
       i-=1
except ValueError:
    print("too low of a number")