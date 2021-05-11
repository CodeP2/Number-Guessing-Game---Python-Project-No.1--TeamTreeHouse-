import random

def start_game():
    print("What would you like to do?    ")
    print("""
    Enter "DONE" if you want to finish the game.
    Enter "TRY" To play the game again.
    """)
print("Welcome to number quessing game!")
question = input("would you like to play the game? (yes/no)")

if question.lower() == "yes":
    Solution = random.randrange(25, 50)
    a = 0
    score = 0 
    while True:
        guess = int(input("What is your guess?   "))
        if guess == Solution:
            print("You got it!")
            print("The number of wrong guesses is", a)
            score += 20
            print("Your total score is:", score)
            print("the best possible score is 20 per game")
            start_game()
            Solution = random.randrange(25, 50)
            quest = input(">    ")
            if quest.upper() == "DONE":
                break
            elif quest.upper() == "TRY":
                guess = input("What is your guess?")
                continue   
        elif guess > 50:
            print("Your number is way too high! Try again!")
            a += 1
            score -= 1
            continue
        elif guess < 25:
            print("Your number is way too low! Try again!")
            a += 1
            score -= 1
            continue
        elif guess > Solution:
            print("Its lower! Try again!")
            a += 1
            score -= 1
            continue
        elif guess < Solution:
            print("Its higher! Try again!")
            a += 1
            score -= 1
            continue
            
