#Quinn Dickey
#5th hour
#Scenario 3
import random
#Now that the game development team has a dictionary for enemies
#(see Scenario 1) and the dictionary for the party is fixed
#(see Scenario 2), they want to start making a full prototype for the
#combat system. The team lead is a big Dungeons & Dragons fan and
#wants to make the combat similar to that. Because of this, the
#dictionaries need to be reworked slightly to be like that.

#Each enemy and party member in both dictionaries needs:
# - health points (somewhere between 6 and 25)
# - an attack modifier (somewhere between 3 and 7)
# - a damage roll (a number that varies based on weapon/spell)
# - and an Armor Class (somewhere between 10 and 17).

#Once both dictionaries are updated, create a combat
#prototype that has a party member attack first, then an enemy
#attacks back right after.

#To determine if a creature hits another creature, you roll a
#20-sided die (d20) and add the attack modifier to the roll.
#If that number is the same as or higher than the enemy's Armor Class
#(AC), the attack hits and you roll for damage. If it is lower, the
#attack misses. If an enemy or party member hits zero (0) health
#points, they die.

#To make things easier, here is a reference list for party damage rolls.
#(Feel free to use similar numbers for your enemy dictionary.)

# - Lae'Zel uses a greatsword: 2d6 + 3
# - Shadowheart uses a mace: 1d6 + 2
# - Gale uses the firebolt spell: 1d10
# - Astarion uses a shortbow: 1d6 + 4




#Party Dictionary Goes Here
partyDictionary = {
    "LaeZel" : {
        "Race" : "Githyanki",
        "Class" : "Fighter",
        "Background" : "Soldier",
        "HP" : 12,
        "AC" : 17,
        "Damage" : 10,
    },
    "Shadowheart" : {
        "Race" : "Half-Elf",
        "Class" : "Cleric",
        "Background" : "Acolyte",
        "HP" : 10,
        "AC" : 14,
        "Damage" : 5,
    },
    "Gale" : {
        "Race" : "Human",
        "Class" : "Wizard",
        "Background" : "Sage",
        "HP" : 8,
        "AC" : 14,
        "Damage" : 17,
    },
    "Astarion" : {
        "Race" : "High Elf",
        "Class" : "Rogue",
        "Background" : "Charlatan",
        "HP" : 10,
        "AC" : 14,
        "Damage" : 12,
    }
}
#Enemy Dictionary goes here
pokeDict= {
    "pokemon001": {
       "name" : "Bulbasaur",
       "HP" : 45,
       "attack" : 48,
       "defense": 49
    },
    "pokemon004": {
        "name": "Charmander",
        "HP" : 39,
        "attack": 52,
        "defense": 43
    },
    "pokemon010": {
        "name": "Caterpie",
        "HP": 45,
        "attack": 30,
        "defense": 35
    },
    "pokemon013": {
        "name": "Weedle",
        "HP" : 40,
        "attack" : 35,
        "defense" :"30"
    }
}

print(pokeDict["pokemon013"]["HP"]-partyDictionary["Gale"]["Damage"])
#Combat Code Goes Here
x=(pokeDict["pokemon013"]["HP"]-partyDictionary["Gale"]["Damage"]+random.randrange(1,20))
y=(partyDictionary["Gale"]["HP"]-pokeDict["pokemon013"]["attack"]+random.randrange(1,20))
if x > 0:
    print("Weedle is still standing!"),
else:
    print("Weedle Passed out! Gale wins!")

y=(partyDictionary["Gale"]["HP"]-pokeDict["pokemon013"]["attack"]+random.randrange(1,20))

if y > 0:
    print("Gale is still satnding!"),
else:
    print("Gale Passed out! Weedle wins!")