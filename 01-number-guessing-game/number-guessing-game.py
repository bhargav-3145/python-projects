import random
player_wants_to_play = True
while player_wants_to_play :
    number = random.randint(1, 100)
    count = 1
    guess = int(input("Enter Your Guess : "))
    while guess != number :
        if (guess > number):
            print("Too high! Try a lower number")
        elif(guess < number):
            print("Too low! Try a higher number")
        guess = int(input("Enter your next guess : "))
        count += 1
    else:
        print(f"Congratulations! You guessed the correct number in {count} attempts")
    while True :
        replay = input("Play again? (Yes or No) : ").lower()
        if replay == "yes":
            break
        elif replay == "no":
            player_wants_to_play = False
            break
        else :
            print("Please enter only Yes or No.")

