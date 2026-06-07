import random
options = ("Rock", "Paper", "Scissors")
player = input("Enter your choice : (Rock, Paper, Scissors) : ").capitalize()
if player not in options:
    print("Choose from (Rock, Paper, Scissors) options only...")
else:
    computer = random.choice(options)
    print(f"Player : {player}")
    print(f"Computer : {computer}")
    if player == computer:
        print("It's a draw")
    elif (
        (player == "Rock" and computer == "Scissors")
        or (player == "Paper" and computer == "Rock")
        or (player == "Scissors" and computer == "Paper")
     ):
        print("Congratulations! You won 🎉")
    else:
        print("Computer won! Good luck next time")
 

