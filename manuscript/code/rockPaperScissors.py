import random

banner = '''
  _____            _                   
 |  __ \          | |                  
 | |__) |___   ___| | __               
 |  _  // _ \ / __| |/ /               
 | | \ \ (_) | (__|   <                
 |_|__\_\___/ \___|_|\_\               
 |  __ \                               
 | |__) |_ _ _ __   ___ _ __           
 |  ___/ _` | '_ \ / _ \ '__|          
 | |  | (_| | |_) |  __/ |             
 |_|   \__,_| .__/ \___|_|             
            | |                        
   _____    |_|                        
  / ____|    (_)                       
 | (___   ___ _ ___ ___  ___  _ __ ___ 
  \___ \ / __| / __/ __|/ _ \| '__/ __|
  ____) | (__| \__ \__ \ (_) | |  \__ \
 |_____/ \___|_|___/___/\___/|_|  |___/
                                       
'''

ROCK     = 0
PAPER    = 1
SCISSORS = 2

keep_going = True

def displayWelome():

    print(banner)
    print()
    print("Rules: rock beats scissors, scissors beats paper, paper beats rock")
    print()

def getUserChoice():
    prompt = ""

    user = int(input("Please enter your choice (0 for rock, 1 for paper, 2 for scissors): "))

    while user not in [0, 1, 2]:
        user = int(input("Please enter a valid choice: "))

    return user

def getCompChoice():
    return random.randint(0, 2)

def evaluteTurn(user, comp):
    # Returns True if the user wins,
    # False if it's a tie or the user loses
    if user == ROCK:
        print("You guessed rock,", end=" ")
    elif user == PAPER:
        print("You guessed paper,", end=" ")
    elif user == SCISSORS:
        print("You guessed scissors,", end=" ")

    if comp == ROCK:
        print("Computer guessed rock.")
    elif comp == PAPER:
        print("Computer guessed paper.")
    elif comp == SCISSORS:
        print("Computer guessed scissors.")

    if (user == ROCK and comp == SCISSORS or
        user == SCISSORS and comp == PAPER or
        user == PAPER and comp == ROCK):
        return 0
    elif user == comp:
        return 1
    else:
        return 2

## Begin Game ##
displayWelome()

while keep_going:
    user = getUserChoice()
    comp = getCompChoice()
    result = evaluteTurn(user, comp)

    if result == 0:
        print("You've won!")
    elif result == 1:
        print("It's a tie.")
    elif result == 2:
        print("You've lost...")

    keep_going = input("Would you like to play again? (yes or no): ").lower().startswith("y")