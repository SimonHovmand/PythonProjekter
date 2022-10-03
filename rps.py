from random import randint

t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0,2)]

player = True

game = True

while player == True:
    if game == False:
        stop = (input("Do you want to continue? Y/N\n"))
        if stop == "Y" or stop == "y":
            player = True
            game = True
        elif stop == "N" or stop == "n":
            break
        else:
            print("invalid!...")
    else:
        player = input("Rock, Paper, Scissors?")
        if player == computer:
            print("Tie!")
        elif player == "Rock":
            if computer == "Paper":
                print("You lose!", computer, "covers", player)
                game = False
            else:
                print("You win!", player, "smashes", computer)
                game = False
        elif player == "Paper":
            if computer == "Scissors":
                print("You lose!", computer, "cut", player)
                game = False
            else:
                print("You win!", player, "covers", computer)
                game = False
        elif player == "Scissors":
            if computer == "Rock":
                print("You lose...", computer, "smashes", player)
                game = False
            else:
                print("You win!", player, "cut", computer)
                game = False
        else:
            print("That's not a valid play. Check your spelling!")
    player =True
    computer = t[randint(0,2)]