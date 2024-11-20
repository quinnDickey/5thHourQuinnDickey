num = int(input("enter a number: "))

factorial = 1
i = 1

while i <= num:
	factorial = factorial * i
	i = i + 1

print("factorial of ", num, " is ", factorial)