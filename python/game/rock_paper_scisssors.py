import random
while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = None
    # print(computer)
    while player not in choices:
        player = input("rock,paper or scissors?").lower()
    if player == computer:
        print("Computer:",computer)
        print("Player:",player)
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("Computer:",computer)
            print("Player:",player)
            print("You lose!")
        if computer == "scissors":
            print("Computer:",computer)
            print("Player:",player)
            print("You win!")
    elif player == "scissors":
        if computer == "rock":
            print("Computer:",computer)
            print("Player:",player)
            print("You lose!")
        if computer == "paper":
            print("Computer:",computer)
            print("Player:",player)
            print("You win!")
    elif player == "paper":
        if computer == "scissors":
            print("Computer:",computer)
            print("Player:",player)
            print("You lose!")
        if computer == "rock":
            print("Computer:",computer)
            print("Player:",player)
            print("You win!")
        
    play_agian = input("Play again? (Yes/No)").lower()
    if play_agian !="yes":
        break
print("Bye!")
