#Name: Quinn Dickey
#Class: 5th Hour
#Assignment: Scenario 2

#Scenario 2:
#The programmer in charge of the player character party stats is
#having some issues with their code. Despite rigorous testing,
#they are inexperienced and can't seem to figure out why the damage
#testing isn't working. Your team lead has asked you to help by fixing
#the party dictionary, insert an enemy into the code below, and
#testing to see if a player character can damage the with a printed
#test that shows the enemy health has changed.


partyDictionary = {
    "LaeZel" : {
        "Race" : "Githyanki",
        "Class" : "Fighter",
        "Background" : "Soldier",
        "Health" : 12,
        "AC" : 17,
        "Damage" : 10,
    },
    "Shadowheart" : {
        "Race" : "Half-Elf",
        "Class" : "Cleric",
        "Background" : "Acolyte",
        "Health" : 10,
        "AC" : 14,
        "Damage" : 5,
    },
    "Gale" : {
        "Race" : "Human",
        "Class" : "Wizard",
        "Background" : "Sage",
        "Health" : 8,
        "AC" : 14,
        "Damage" : 17,
    },
    "Astarion" : {
        "Race" : "High Elf",
        "Class" : "Rogue",
        "Background" : "Charlatan",
        "Health" : 10,
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
    },
    "pokemon004": {
        "name": "Charmander",
        "HP" : 39,
        "attack": 52,
    },
    "pokemon007": {
        "name": "Squritle",
        "HP": 44,
        "attack" : 48,
    },
    "pokemon010": {
        "name": "Caterpie",
        "HP": 45,
        "attack": 30,
    },
    "pokemon013": {
        "name": "Weedle",
        "HP" : 40,
        "attack" : 35,
    }
}

print(pokeDict["pokemon013"]["HP"]-partyDictionary["Gale"]["Damage"])

#Test the damage here by subtracting a party member's damage from the enemy's health.
