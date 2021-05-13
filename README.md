# Number Guessing Game - Python Project No.1 (TeamTreeHouse)
 
This is my 1st project
I know it dosen't show the if the number is higher or lower but this might not be the best solution with ("Press 1 to continue") 
but for now its good I suppouse I was thinking about how to make it appear and chaning the order messes up my code so this might be the 
best solution for now altho I would like to know more,
I was using my workshop for this project I couldn't fing anything much helpful for this project on google
so I was only using my workshop codes to help me if anything
I know my code is not perfect but if it is possible I would like to get feedback what I could do better
Update:
so I spend quite some time to solve me issues with code but I got there (mostly because of order) but it is working so I had to use this:
https://docs.python.org/3/library/stdtypes.html#list.sort 
function and because I had error about for i in X because loop for will not do for int I had to change it but this post made me understand:
https://stackoverflow.com/questions/19523563/python-typeerror-int-object-is-not-iterable
as for code usege I couldn't really find anything but at least I got function that helped me to do the high score if anythin I was using my workshop codes to help me so I can't really link them but I kind of combined all of the lessons I had well I was watching
Also I had issue with try block well mostly it was with order or I would say missing except I spend well some time to figure it out but I don't really want ot use google too much or at all if possible but for the condition I was using and but for python language its both condition must be true so thats why I changed to or I was ohh it bool 
"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.



# Kick off the program by calling the start_game function.
start_game()
     
