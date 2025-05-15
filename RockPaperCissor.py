import random

def play_game():
    valid_choices = ['rock', 'paper', 'scissors']
    while True:
        user = input("Enter your choice (rock, paper, scissors) or 'quit' to exit: ").strip().lower()
        if user == 'quit':
            print("Thanks for playing! Goodbye.")
            break
        if user not in valid_choices:
            print("Invalid choice. Please enter 'rock', 'paper', 'scissors', or 'quit'.")
            continue

        computer = random.choice(valid_choices)
        print(f"Computer chose: {computer}")

        if user == computer:
            print("It's a tie!")
        elif (user == 'rock' and computer == 'scissors') or \
             (user == 'paper' and computer == 'rock') or \
             (user == 'scissors' and computer == 'paper'):
            print("You win!")
        else:
            print("You lose!")

if __name__ == "__main__":
    play_game()
