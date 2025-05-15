import random

def guess(x):
    if x < 1:
        print("The upper limit must be at least 1.")
        return
    random_number = random.randint(1, x)
    guess = None
    while guess != random_number:
        try:
            guess = int(input(f'Guess a number between 1 and {x}: '))
            if guess < 1 or guess > x:
                print(f'Please enter a number within the range 1 to {x}.')
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
        else:
            print(f'Yay! You guessed the number {random_number} correctly!')

def computer_guess(x):
    if x < 1:
        print("The upper limit must be at least 1.")
        return
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' and low <= high:
        guess = random.randint(low, high)
        print(f"Computer guesses: {guess}")
        feedback = input("Is it too high (H), too low (L), or correct (C)? ").lower().strip()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f"Yay! The computer guessed your number {guess} correctly!")
            return
        else:
            print("Invalid input. Please enter H, L, or C.")

    if low > high:
        print("It seems there was a contradiction in your answers. Please restart the game.")

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 1:
                print("Please enter a positive integer greater than zero.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    print("Welcome to the Number Guesser game!")
    print("Choose a mode:")
    print("1 - You guess the number")
    print("2 - Computer guesses your number")
    mode = input("Enter 1 or 2: ").strip()

    if mode == '1':
        x = get_positive_integer("Enter the upper limit for the random number: ")
        guess(x)
    elif mode == '2':
        x = get_positive_integer("Enter the upper limit for the computer to guess: ")
        computer_guess(x)
    else:
        print("Invalid mode selected. Please restart the game and choose either 1 or 2.")


