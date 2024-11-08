#Name:Quinn Dickey
#Class: 5th Hour
#Assignment: HW12
import time
import random
from audioop import reverse
from importlib.metadata import pass_none

#1. Create a for loop with variable i that counts down from 5 to 1
#and then prints "Hello World!" at the end.


for i in range(5,0,-1):
    print(i)
else:
    print("hello world")

    #2.Create a for loop that counts up and prints only even numbers
# between 1 and 30.
# (HINT: Look back to HW6 on how to see if a number is divisible by another)
for b in range(1,31):
    if i % 2==0:
        print(i)
else:
    pass
# 3. Create a for loop that prints 5 different animals from a list.
animal=["dog","cat","fish","bird","snake"]
for y in animal:
    print(y)

# 4. Create a for loop that spells out a word you input backwards.
# (HINT: Google "How to reverse a string in Python")

for k in input("give a word:"):
    print(k)