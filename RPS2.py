import random
def playround(choice):
    winloss = ["rock", "paper", "scissors", "paper", "scissors", "rock", "scissors", "rock", "paper"]
    computerchoice = random.randint(0,2)
    print(winloss[computerchoice]) #Print the computers' selection
    if choice == winloss[computerchoice+3]:
        return "You win!", 1, 0   #The user wins if the have whatever the user loses to (row 1)
    elif choice == winloss[computerchoice+6]:
        return "You lose!", 0, 1  #The user loses if they have whatever the computer wins to (row 2)
    elif choice == winloss[computerchoice]:
        return "Draw!", 0, 0      #The user wins if they have the same as the computer (row 0)
    else:
        return "error", 0, 0
winsandlosses = [0,0]
while True:
    userchoice = input("======================\nRock, paper, scissors!\n======================\n")
    play = playround(userchoice.lower())
    winsandlosses[0] += play[1]
    winsandlosses[1] += play[2]
    again = input(f"{play[0]}\nWins: {winsandlosses[0]} Losses: {winsandlosses[1]}\nPlay again (y/n)?")
    if again.lower()=="n":
        break
