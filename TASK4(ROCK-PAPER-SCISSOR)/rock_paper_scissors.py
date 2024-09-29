import tkinter as tk
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "You Win!"
    else:
        return "You Lose!"

# Function to play the game
def play(choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = determine_winner(choice, computer_choice)
    
    # Update the result labels
    user_choice_label.config(text=f"Your Choice: {choice}", fg="white")
    computer_choice_label.config(text=f"Computer's Choice: {computer_choice}", fg="white")
    result_label.config(text=result, fg="white")

    # Update scores
    if result == "You Win!":
        global user_score
        user_score += 1
    elif result == "You Lose!":
        global computer_score
        computer_score += 1
    
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}", fg="white")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}", fg="white")
    user_choice_label.config(text="Your Choice: ", fg="white")
    computer_choice_label.config(text="Computer's Choice: ", fg="white")
    result_label.config(text="", fg="white")

# Initialize global scores
user_score = 0
computer_score = 0

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x400")
root.configure(bg="black")  # Black background

# Create and place the widgets
instructions_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", bg="black", fg="white", font=('Arial', 14))
instructions_label.pack(pady=10)

# Buttons for choices with new color
rock_button = tk.Button(root, text="Rock", command=lambda: play("Rock"), bg="#FF5733", fg="white", font=('Arial', 12))  # Red
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", command=lambda: play("Paper"), bg="#33FF57", fg="white", font=('Arial', 12))  # Green
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", command=lambda: play("Scissors"), bg="#3357FF", fg="white", font=('Arial', 12))  # Blue
scissors_button.pack(pady=5)

# Labels to display choices and results
user_choice_label = tk.Label(root, text="Your Choice: ", bg="black", fg="white", font=('Arial', 12))
user_choice_label.pack(pady=5)

computer_choice_label = tk.Label(root, text="Computer's Choice: ", bg="black", fg="white", font=('Arial', 12))
computer_choice_label.pack(pady=5)

result_label = tk.Label(root, text="", bg="black", fg="white", font=('Arial', 12))
result_label.pack(pady=10)

# Score tracking label
score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", bg="black", fg="white", font=('Arial', 12))
score_label.pack(pady=10)

# Reset game button with new color
reset_button = tk.Button(root, text="Reset Game", command=reset_game, bg="#E74C3C", fg="white", font=('Arial', 12))  # Dark red
reset_button.pack(pady=10)

# Run the main loop
root.mainloop()
