#Name:Quinn Dickey
#Class: 5th Hour
#Assignment: HW16
import random
#1. Create a def function that plays a single round of rock, paper, scissors where
# the user inputs 1 for rock, 2 for paper, or 3 for scissors and compares it to
#a random number generated to serve as the "opponent's hand".
print("hello world!")
import random
def the_game():
    the_player= int(input("please enter the number: rock(1), paper(2), scissors(3)"))
    computerplayer = random.randint(1, 3)

    print(f"Opponent chose {computerplayer}")
    if the_player == 1 :
        if computerplayer ==1:
            print("tie")
        if computerplayer ==2:
            print("computer wins!")
        if computerplayer ==3:
            print("you win!")
    else:
        print("")

    if the_player ==2 :
        if computerplayer ==1:
            print("you win!")
        if computerplayer ==2:
            print("tie")
        if computerplayer ==3:
            print("computer wins!")
    else:
        print("")

    if the_player == 3:
        if computerplayer == 1:
            print("Computer wins!")
        if computerplayer == 2:
            print("you win!")
        if computerplayer == 3:
            print("tie!")
    else:
        print("")

the_game()


replayInput = input("Would you like to play again? Y/N (case-sensitive) ")

if replayInput == "Y":
    the_game()
else:
    exit()


#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.