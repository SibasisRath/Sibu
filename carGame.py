print('''This is a car game. It can be played like this---
first You have to start the game by typing 'start' and 
then the journey will be started. If you want to stop the 
car, then just type "park".Finally if you want to quit, 
then just type "q" to stop the game. ''')

while True:
    a=input("")
    if a=="start":
        print ("\nThe journey is Started.")
        p=input("Where do you want to go?\n")
        print("we are going to "+p)
    elif a=="park":
        print("\nYour car is parked. Your journey is stopped.")
        print("If you have reached Press \'q\' to stop. or press \'r\' to continue")
    elif a=="r":
        print("\nYour journey is continu")
        pass
    elif a=="q":
        print("\nYou quit.")
        break
    else:
        print("\nThe game didn't get it.")
print("\nThank you for playing.")
