import random

def play_game():
    valid_choices = ['rock', 'paper', 'scissors']
    while True:
        user = input("Enter your choice (rock, paper, scissors): ").strip().lower()
        if user not in valid_choices:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            continue
        break

    computer = random.choice(valid_choices)
    print(f"Computer chose: {computer}")

    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "You lose!"

if __name__ == "__main__":
    result = play_game()
    print(result)
