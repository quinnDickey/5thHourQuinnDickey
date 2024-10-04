#Quinn Dickey
#5th hour
#playground
# https://blog.enterprisedna.co/python-shuffle-list/
from random import shuffle, random
from turtledemo.sorting_animate import randomize

print("hello world")

numbList =[1,2,3,4,5,6,7,8,9,10]

print(numbList)
print("Guess a number between 1 and 10")
x=int(input())
shuffle(numbList)
print(numbList[1])
if numbList [1] == x:
    print("win")
else:
    print("loss")

