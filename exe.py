import random

guess = random.randint(0,1000)
print(guess)
user = int(input("Enter your guess: "))


if user == guess:
    print("You win!")
else :
    print("You lose!")



