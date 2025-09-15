import tkinter as tk
import random

# Main Window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x400")
root.config(bg="#f0f0f0")

# Global Variables
user_score = 0
computer_score = 0
choices = ["Rock", "Paper", "Scissors"]

# Functions
def play(user_choice):
    global user_score, computer_score
    
    computer_choice = random.choice(choices)
    result = ""

    if user_choice == computer_choice:
        result = "It's a Tie 🤝"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You Win 🎉"
        user_score += 1
    else:
        result = "You Lose 💀"
        computer_score += 1

    # Update Labels
    user_choice_label.config(text=f"You chose: {user_choice}")
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=result)
    score_label.config(text=f"Score: You {user_score} - {computer_score} Computer")


def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_choice_label.config(text="You chose: ")
    computer_choice_label.config(text="Computer chose: ")
    result_label.config(text="Let's Play!")
    score_label.config(text=f"Score: You 0 - 0 Computer")

# Widgets
title_label = tk.Label(root, text="🎮 Rock Paper Scissors 🎮", font=("Arial", 18, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

user_choice_label = tk.Label(root, text="You chose: ", font=("Arial", 14), bg="#f0f0f0")
user_choice_label.pack()

computer_choice_label = tk.Label(root, text="Computer chose: ", font=("Arial", 14), bg="#f0f0f0")
computer_choice_label.pack()

result_label = tk.Label(root, text="Let's Play!", font=("Arial", 16, "bold"), fg="blue", bg="#f0f0f0")
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score: You 0 - 0 Computer", font=("Arial", 14), bg="#f0f0f0")
score_label.pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)

rock_btn = tk.Button(button_frame, text="🪨 Rock", font=("Arial", 12), width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(button_frame, text="📄 Paper", font=("Arial", 12), width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(button_frame, text="✂️ Scissors", font=("Arial", 12), width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5)

reset_btn = tk.Button(root, text="🔄 Reset Game", font=("Arial", 12), command=reset_game)
reset_btn.pack(pady=20)

# Run App
root.mainloop()
