#Name:Quinn Dickey
#Class: 5th Hour
#Assignment: HW10
import time

#1. Create a while loop with variable i that counts down from 5 to 0
#and then prints "Hello World!" at the end.

i=5
while i >= 0:
    print(i)
    time.sleep(.5)
    i-= 1
else:
    print("Hello world!")
#2. Create a while loop that prints only even numbers
#between 1 and 30.
j=30
while j>=0:
    j-=1
    if j % 2== 0:
     print(j)
#3. Create a while loop that repeats until the user
#inputs the number 0.
print("x")

x = 1
z=int(input("guess a number"))
while x>=0:
    x=x+1
    print(x)
    if z==0:
        break

