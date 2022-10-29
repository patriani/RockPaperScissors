from random import choice

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer_choice = lambda x:choice(x).lower()

print("use :quit to exit")

while True:
    computer = computer_choice(t)

    player = input(",".join(t)+"? ").strip().lower()

    if player == computer:
        print("Tie!")

    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)

    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)

    elif player == "scissors":
        if computer == "rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)

    else:
        if player == ":quit":
            break
        else:
            print("That's not a valid play. Check your spelling!")

    
