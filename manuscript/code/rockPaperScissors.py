import random

banner = '''
__________               __                           
\______   \ ____   ____ |  | __                       
 |       _//  _ \_/ ___\|  |/ /                       
 |    |   (  <_> )  \___|    <                        
 |____|_  /\____/ \___  >__|_ \                       
        \/            \/     \/                       
__________                                            
\______   \_____  ______   ___________                
 |     ___/\__  \ \____ \_/ __ \_  __ \               
 |    |     / __ \|  |_> >  ___/|  | \/               
 |____|    (____  /   __/ \___  >__|                  
                \/|__|        \/                      
  _________      .__                                  
 /   _____/ ____ |__| ______ _________________  ______
 \_____  \_/ ___\|  |/  ___//  ___/  _ \_  __ \/  ___/
 /        \  \___|  |\___ \ \___ (  <_> )  | \/\___ \ 
/_______  /\___  >__/____  >____  >____/|__|  /____  >
        \/     \/        \/     \/                 \/ 
'''

ROCK     = 0
PAPER    = 1
SCISSORS = 2

keep_going = True

def displayWelome():
    rules = "Rules: rock beats scissors, "
    rules += "scissors beats paper, "
    rules += "paper beats rock"

    print(banner)
    print()
    print(rules)
    print()

def getUserChoice():
    prompt = "Please enter your choice "
    prompt += "(0 for rock, 1 for paper, 2 for scissors): "

    user = int(input(prompt))

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

    prompt = "Would you like to play again? "
    prompt += "(yes or no): "

    keep_going = input(prompt)
    keep_going = keep_going.lower().startswith("y")