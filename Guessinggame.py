import random

def start_game():
    print("What would you like to do?    ")
    print("""
    Enter "DONE" if you want to finish the game.
    Enter "TRY" To play the game again.
    """)
print("Welcome to number quessing game!\nIn this game you choose a number in range of 25-49 good luck and have fun !")
question = input("would you like to play the game? (yes/no)")
if question.lower() == "yes":
    Solution = random.randrange(25, 50)
    a = 0
    X = [20, ]
    b = min(X)
    print("the best score so far (score is based on how many wrong guesses you made):", b)
    while True:
        try:
            guess = int(input("What is your guess?   "))  
            if guess > 49 or guess < 25:
                raise ValueError("oh uh we run into an issue!")
            
        except ValueError as err:
            print("Your number is too high/low and make sure it is number! Please try again!")
            
        else:
            if guess == Solution:
                print("You got it!")
                print("The number of wrong guesses is", a)
                X.append(int(a))
                b = min(X)
                print("the best score so far:", b)
                start_game()
                Solution = random.randrange(25, 50)
                quest = input(">    ")
                if quest.upper() == "DONE":
                    print("Thank you for playing the game!")
                    break
                elif quest.upper() == "TRY":
                    a = 0
                    b = min(X)
                    print("the best score so far:", b)
                    continue   
            elif guess > Solution:
                print("Its lower! Try again!")
                a += 1
                continue
            elif guess < Solution:
                print("Its higher! Try again!")
                a += 1
                continue
            elif guess > 49:
                raise ValueError("oh uh we run into an issue!")
                continue
