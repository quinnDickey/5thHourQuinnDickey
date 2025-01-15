#Name:Quinn Dickey
#Class: 5th Hour
#Assignment: HW15

#1. Create a def function that prints out "Hello World!"
def hello_world():
    print("Hello world")

#2. Create a def function that calculates the average of three numbers.

#3. Create a def function with the names of 5 animals as arguments, treats it like a list, and
#prints the name of the third animal.

def average(a,b,c):
    print(a+b+c//3)



def animals_list(*animal):
    print("the 3rd animal is",animal[2])


#4. Create a def function that loops from 1 to the number put in the argument.

def count(x):
    for x in range(6):
        print(x)

#5. Call all of the functions created in 1 - 4 with relevant arguments.

hello_world()
average(a=8,b=4,c=12)
count(5)
animals_list("cat","dog","bird","fish","fly")
