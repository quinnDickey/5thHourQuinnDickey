#Name:Quinn Dickey
#Class: 5th Hour
#Assignment: HW24

import random
import time

#1. Copy over your class from HW23 and all the functions inside of it, and alter any functions to use self if applicable.
class Classes:
    def __init__(self,health,damage,speed,max_health):
        self.health=health
        self.damage=damage
        self.speed=speed
        self.max_health=max_health
    def repetedamage(self):
        for i in range(10):
            self.health -= random.randint(1,6)
            print(self.health)
    def healingdamge(self):
        self.health+=30
        if self.health > 100:
            self.health=100

warrior= Classes(100,20,30,100)
healer= Classes(60,10,30,60)
thief=Classes(50,30,40,50)
mage=Classes(45,35,25,45)

#2. Create a fourth attribute in the class called max_health that has the same values as health

#3. Copy the warrior and healer objects from HW23, and then make two more character objects with the following attribute values: thief (health/max: 50, damage: 30, speed: 40) and mage (health/max: 45, damage:35, speed: 25)

#4. Randomly choose one of the four character objects to take the damage over time function and call the function to them
randchoice=random.choice((warrior,healer,thief,mage))

randchoice.repetedamage()
#5. Determine who lost health by comparing the current health to the max_health and heal that character object by calling your healing function to that object and then print their health afterwards.
print(f"health stats Warrior: {warrior.health},healer: {healer.health},thief:{thief.health},mage:{mage.health}")
print(f"health stats Warrior: {warrior.max_health},healer: {healer.max_health},thief:{thief.max_health},mage:{mage.max_health}")
randchoice.healingdamge()
print(f"health stats Warrior: {warrior.health},healer: {healer.health},thief:{thief.health},mage:{mage.health}")
print(f"health stats Warrior: {warrior.max_health},healer: {healer.max_health},thief:{thief.max_health},mage:{mage.max_health}")