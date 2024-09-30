import random

user_score = 0
computer_score = 0

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play_round():
    global user_score, computer_score

    user_choice = input("Choose rock, paper, or scissors: ").lower()

    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please choose either 'rock', 'paper', or 'scissors'.")
        return

    computer_choice = get_computer_choice()

    winner = determine_winner(user_choice, computer_choice)

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
        user_score += 1
    else:
        print("You lose!")
        computer_score += 1

    print(f"Score - You: {user_score}, Computer: {computer_score}\n")

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
 
    while True:
        play_round()

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes": 
            break

    print("\nThank you for playing!")
    print(f"Final Score - You: {user_score}, Computer: {computer_score}")

play_game()
