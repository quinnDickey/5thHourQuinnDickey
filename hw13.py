#Name: Quinn Dickey
#Class: 5th Hour
#Assignment: HW13


#1. Create a list containing 10 integers of your choice.
numberList=[1,6,12,8,3,88,11,7,4,18]
#2. Create two empty variables named evenNumbers and oddNumbers.
evenNumbers=0
oddNumbers=0
#3. Make a loop that counts the number of even and odd numbers in the list.
#(HINT: The way to see if a number is even is if it is divisible by 2).
for num in numberList:
    if num % 2 == 0:
        evenNumbers += 1
    else:
        oddNumbers += 1
# Print the total count of even and odd numbers.
print("even number:", evenNumbers)
print("odd numbers:", oddNumbers)