#Name: Quinn Dickey, Gabe
#Class: 5th Hour
#Assignment: Scenario 5
import random

print("Hello World!")

#Scenario 5
#You're all part of a new development team and the big wigs want to see what you are all capable of.
#They want you to develop whatever you want to develop, but there's only one problem:
#the same big wigs only bought enough computers for half of you. Because of this, you will
#all be split into teams of two. One serving as the brain (not using the computer),
#one serving as the hands (using the computer).

lootbox1 = ["skin1","skin2", "skin3","skin4"]
lootbox2= None
k=int(input("how many lootbox keys do you have?"))
for k in range(k):
    new_item = random.choice(lootbox1)
    if k == 0:
        lootbox2 = new_item
        print(f"your first item;{lootbox2}")
    elif new_item == lootbox2:
        print(f"next item is;{new_item} (duplicate)")
    else:
        print(f"your next item; {new_item}")

if k >0:
    print("thank you! come again")
#if


#You have until the Scenario is due to brainstorm an idea together, create a flowchart, and then
#turn that flowchart into functioning code. The code itself must have at least:
# 1 dictionary or list,
#1 loop,
#2 if statements (elif and else statements tied to it does not count towards the total),
#1 variable with a user input,
#and 1 form of an assignment operator.

#you are free to add whatever else you feel is necessary to complete your concept.
#You will be graded based on how those ideas are implemented together.