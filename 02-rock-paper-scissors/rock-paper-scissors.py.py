import random
options = ("Rock", "Paper", "Scissors")
player = input("Enter your choice (Rock, Paper or Scissors) : ").capitalize()
if player not in options :
    print("choose from given options only : ")
else:
    computer = random.choice(options)
    print("Player : ", player)
    print("Computer : ", computer)
    if player == computer :
           print("It's a draw")
    elif player == "Rock" and computer == "Scissors":
        print("player wins! 🪨")
    elif player == "Paper" and computer == "Rock":
        print("player wins! 🗞️ ")
    elif player == "Scissors" and computer == "Paper":
        print("player wins! ✂️")
    else:
        print("computer wins!")
 

