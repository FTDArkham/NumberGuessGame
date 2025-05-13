# Import stuff 
import random
import time
# Variables 
end = False
# Beginning 
while not end:
    print("Hi I'm the number guessing game!!!")
    start = input("Would you like to play a game?(Y/N): ")
    if (start == "Y" or start == "y"):
        print("Alright, Let's go!!!!")
        print()
        time.sleep(1)
        play = True
        while play:
# Difficulty
            print("What difficulty would you like?")
            print("1. Easy (10 Chances)")
            print("2. Medium (5 Chances)")
            print("3. Hard (3 Chances)")
            print("4. Impossible (1 Chance)")
            diff = input("Enter Selection (1, 2, 3, or 4): ")
            print()
            match diff:
                case "1":
                    print ("You chose easy")
                    n = 10
                case "2":
                    print ("You chose medium")
                    n = 5
                case "3":
                    print ("You chose hard")
                    n = 3
                case "4": 
                    print ("You chose hard")
                    n = 1
                case _:
                    print("No valid selection made. Defaulting to medium")
                    n = 5
# Picks a Number
            print()
            print("I'm going to pick a number between 1 and 100, and all you have to do is guess it!!!")
            randnumber = random.randint(1, 100)
# Guess
            for number in range(int(n)):
                print()
                guess = input("Take your guess: ")
                if int(guess) == randnumber:
                    print("Congrats!!! You're a lucky cookie. You got the right answer in ", number + 1, " guesses")
                    break
                elif number < n-1:
                    if int(guess) < randnumber: # Tells the player whether they are higher or lower than the correct number
                        print("Not quite. Try higher")
                    else:
                        print("Not quite. Try Lower")
                else:
                    print("Oof better luck next time. The correct answer was", (randnumber))
# Play agiain
            print()
            playmore = input("Would you like to play again? (Y/N): ") # Gives the player the option to keep going if they want
            if (playmore == "Y" or playmore == "y"):
                print("Yay! Let's go again")
                print()
            else:
                print()
                print ("See you next time")
                play = False
    end = True

print("GAME OVER")