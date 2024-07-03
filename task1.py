import random

guess = random.randint(0, 1000)

print("Guess the number between 0 and 1000")

while True:
    user_input = input("Enter your guess (or use <number or >number): ")

    if user_input.startswith("<"):
        try:
            number = int(user_input[1:])
            if number > guess:
                print("Yes")
            else:
                print("No")
        except ValueError:
            print("Invalid input. Please enter a valid number after '<'.")
    elif user_input.startswith(">"):
        try:
            number = int(user_input[1:])
            if number < guess:
                print("Yes")
            else:
                print("No")
        except ValueError:
            print("Invalid input. Please enter a valid number after '>'.")
    else:
        try:
            user = int(user_input)
            if user == guess:
                print("You win!")
                break
            elif user < guess:
                print("Too low!")
            else:
                print("Too high!")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
