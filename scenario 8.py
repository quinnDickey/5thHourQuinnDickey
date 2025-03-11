#Name:
#Class: 5th Hour
#Assignment: Scenario8
import random



#Scenario 8:
#With a fresh perspective, the team lead wants you to look back and refactor the old combat code to
#be streamlined with classes so the character and enemy stats won't be built in bulky dictionaries anymore.

#(Translation: Rebuild Scenario 3 using classes instead of dictionaries, include the combat test code
#below as well.)

class Party:
    def __init__(self,HP,AC,Damage):
        self.HP=HP
        self.AC=AC
        self.Damage=Damage

class Poke:
    def __init__(self, HP,attack,defense):
        self.HP=HP
        self.attack=attack
        self.defense=defense

Bulbasaur= Poke(45,48,49)
Charmander= Poke(39,52,43)
Caterpie= Poke(45,30,35)
Weedle= Poke(40, 35,30)

LaeZel= Party(12,17,10)
Shadowheart= Party(10,14,5)
Gale= Party(8,14,17)
Astarion= Party(10,14,12)

y=Bulbasaur.HP-Gale.Damage
if y > 0:
    print("Bulbasaur is still standing!"),
else:
    print("Bulbasaur Passed out! Gale wins!")

x=Gale.HP-Bulbasaur.attack
if x > 0:
    print("Gale is still standing!"),
else:
    print("Gale Passed out! Bulbasaur wins!")

