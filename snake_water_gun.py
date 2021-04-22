'''Snake vs. Water: Snake drinks the water hence wins.
Water vs. Gun: The gun will drown in water, hence a point for water
Gun vs. Snake: Gun will kill the snake and win.'''


print('''Let's play SNAKE WATER GUN game.
Rules are :-Snake vs. Water: Snake drinks the water hence wins.
Water vs. Gun: The gun will drown in water, hence a point for water
Gun vs. Snake: Gun will kill the snake and win.If you want to quit just press "q"\n\n\n\n''')

import random


while True:
    userInput=input("You have to type \'s\' for snake, \'w\' for water and \'g\' for gun.\n\nYour guess: ")
    pc=['s','g','w']
    pcshow=random.choice(pc)
    print("The pc choose: "+pcshow)
    if userInput=='s':
        if pcshow=='s':
            print("It's a tie.")
        elif pcshow=='g':
            print("pc won.")
        elif pcshow=='w':
            print("User won.")
    elif userInput=='g':
        if pcshow=='g':
            print("It's a tie.")
        elif pcshow=='s':
            print("pc won.")
        elif pcshow=='w':
            print("User won.")
    elif userInput=='w':
        if pcshow=='w':
            print("It's a tie.")
        elif pcshow=='s':
            print("pc won.")
        elif pcshow=='g':
            print("User won.")  
    elif userInput=="q":
        break
    else:
        print("The game didn't get it.") 

print("\n\n\nThank You for playing. \n\nDesigned by SIBASIS RATH.\n\n\n")
