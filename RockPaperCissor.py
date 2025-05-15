import random

def play_game():
    valid_choices = {
        'rock': 'rock',
        'r': 'rock',
        'paper': 'paper',
        'p': 'paper',
        'scissors': 'scissors',
        's': 'scissors'
    }
    quit_commands = ['q', 'quit']

    while True:
        user_input = input("Enter your choice (rock/r, paper/p, scissors/s) or 'q'/'quit' to exit: ").strip().lower()
        if user_input in quit_commands:
            print("Thanks for playing! Goodbye.")
            break
        if user_input not in valid_choices:
            print("Invalid choice. Please enter rock/r, paper/p, scissors/s, or q/quit to exit.")
            continue

        user = valid_choices[user_input]
        computer = random.choice(['rock', 'paper', 'scissors'])
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
