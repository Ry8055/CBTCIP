# CipherByte Python Task 
# rock_paper_scissor game 
# by --> Ravi Yadav


import tkinter as tk
from tkinter import ttk
import random

def play_game(player_choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = determine_winner(player_choice, computer_choice)
    display_result(player_choice, computer_choice, result)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def display_result(player_choice, computer_choice, result):
    result_text.set(f"Player: {player_choice.capitalize()}\nComputer: {computer_choice.capitalize()}\nResult: {result}")

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x300")

# Create style for buttons
style = ttk.Style()
style.configure('TButton', font=('Arial', 14))

# Create widgets
instruction_label = ttk.Label(root, text="Choose your move:", font=('Arial', 16))
instruction_label.pack(pady=10)

button_frame = ttk.Frame(root)
button_frame.pack()

rock_button = ttk.Button(button_frame, text="Rock", command=lambda: play_game("rock"))
rock_button.grid(row=0, column=0, padx=10, pady=5)

paper_button = ttk.Button(button_frame, text="Paper", command=lambda: play_game("paper"))
paper_button.grid(row=0, column=1, padx=10, pady=5)

scissors_button = ttk.Button(button_frame, text="Scissors", command=lambda: play_game("scissors"))
scissors_button.grid(row=0, column=2, padx=10, pady=5)

result_text = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_text, font=('Arial', 14))
result_label.pack(pady=20)

# Run the main event loop
root.mainloop()
