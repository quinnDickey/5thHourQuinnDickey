#Name: Quinn Dickey
#Class: 5th Hour
#Assignment: HW18

import random

#1. Import the "random" library and create a def function that prints "Hello World!"
def welcoming():
    print("hello world !")

#2. Create a list called beanBag and add at least 5 different colored beans to the list as strings.
Beanbag=["yellow","blue","red","green","purple"]
#3. Create a def function that pulls a random bean out of the beanBag list, prints which bean you pulled, and then removes it from the list.
def bag_pull():
    if not Beanbag:
        print("No Beanbag!")
        exit()
    else:
        hand = random.choice(Beanbag)
        print(hand)
        Beanbag.remove(hand)
        repeat_bean()
#4. Create a def function that asks if you want to pull another bean out of the bag and, if yes, repeats the #3 def function
def repeat_bean():
    userrepeat = input("Do you want to pull another beanbag? Y/N")
    if userrepeat == "Y" or userrepeat == "y":
        bag_pull()
    elif userrepeat == "N" or userrepeat == "n":
        exit()
    else:
        print("Input not valid. Try again")
#5. Call the #3 function at the bottom.
welcoming()
bag_pull()
