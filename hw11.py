#Name:Quinn Dickey
#Class: 5th Hour
#Assignment: HW11

#A common exercise in computer science is "FizzBuzz". The rules of
#the game are simple. Count from 1 to 100 but with every number that
#is divisible by 3 you say "Fizz" instead of the number,
#every number divisible by 5 you say "Buzz" instead,
#and if it's divisible by both you say "FizzBuzz".

#Create a while loop that follows the rules of the game.
#(HINT: Look back to HW6 on how to see if a number is divisible by another)
j=0
while 100>j:
    j+=1
    if j %5 ==0 and j%3==0:
        print("fizzbuzz")

    elif j % 5 ==0:
        print("buzz"),

    elif j % 3== 0:
        print("fizz"),

    else:
        print(j)