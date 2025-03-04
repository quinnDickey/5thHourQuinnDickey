#Name:Quinn Dickey
#Class: 5th Hour
#Assignment: HW21
from operator import truediv
from xml.dom.minidom import CDATASection

#1. Make a nested dictionary with three entries called "sport1", "sport2", and "sport3" containing
#the name a sport the school partakes in, the amount of players a typical team uses during gameplay
#(ex: Basketball has 5 players), and if the sport uses a ball or not (as a boolean).
has_ball=True
no_ball=False
sports={
    "sport1": {
    "name": "basketball",
    "number":5,
    "has_ball": True
    },
     "sport2": {
    "name": "football",
    "number":11,
    "has_ball": True
    },
    "sport3": {
    "name": "soccer",
    "number":11,
    "has_ball": True
    },
}

#2. Create a def function that pulls the values from the dictionary as arguments, adds together the
#players of all three sports, and prints the sum
def players_sum(a,b,c):
    players_sum = a + b + c
    print(players_sum)
#3. Call the function with arguments here
players_sum(sports["sport1"]["number"], sports["sport2"]["number"] , sports["sport3"]["number"])
