#Name:Quinn Dickey
#Class: 5th Hour
#Assignment: Scenario 4

#Scenario 4:
#Due to scope creep leading to high development costs, the RPG you were working on has been
#shelved for the time being. You have been transferred to a new team working on a mobile game
#that allows you to dress up a model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.

print("hello world")
z=0
x=int(input("how many players?"))
for i in range(0,x):
    y=(int(input("Rank the outfit 1 to 5"))),

avg=sum(y)/len(y)

print(avg)
