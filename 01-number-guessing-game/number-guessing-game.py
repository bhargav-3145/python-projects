import random
number = random.randint(1, 100)
guess = int(input("Enter Your Guess : "))
while guess != number :
    if (guess > number):
        print("Too high! Try a lower number")
    elif(guess < number):
        print("Too low! Try a higher number")
    guess = int(input("Enter your next guess : "))
else:
    print("Congratulations, You guessed the correct number")