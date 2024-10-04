#Quinn Dickey
#Scenario 1
#5th hour

print("hello world")

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


pokeDict["pokemon013"]["attack"]=int(input("Attack power for Weedle"))

pokeDict["pokemon010"]["attack"]=int(input("Attack power for Caterpie"))

pokeDict["pokemon007"]["attack"]=int(input("Attack power for Squritle"))

pokeDict["pokemon004"]["attack"]=int(input("Attack power for Charmander"))

pokeDict["pokemon001"]["attack"]=int(input("Attack power for Bulbasaur"))
print(pokeDict)
