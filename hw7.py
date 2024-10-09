#Quinn Dickey
#5th hour
#HW7

print("hello world")

wifi = True
login = True
admin = True

boss = 0

if wifi == True:
    if login == True:
        if admin == True:
            print("Welcome Admin!")
            boss += 1
            print(boss)
        else:("No admin access.")
    else:print("Login in failed. Try a different password or username")
else:print("No internet access. Please connect to the internet")