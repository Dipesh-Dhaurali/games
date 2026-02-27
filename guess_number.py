import tkinter as tk
import random

root = tk.Tk()
root.title("Guess the Number 1–50")

target = random.randint(1, 50)
attempts = 0

info = tk.Label(root, text="Enter a number between 1 and 50", font=("Arial", 14))
info.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 5))

entry = tk.Entry(root, font=("Arial", 16), width=6, justify="center")
entry.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
entry.focus_set()

feedback = tk.Label(root, text="", font=("Arial", 14))
feedback.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

status = tk.Label(root, text="Attempts: 0", font=("Arial", 12))
status.grid(row=3, column=0, columnspan=2, padx=10, pady=(0, 10))

history_label = tk.Label(root, text="History", font=("Arial", 12))
history_label.grid(row=4, column=0, columnspan=2, padx=10, pady=(0, 5), sticky="w")

history = tk.Listbox(root, font=("Arial", 12), height=6)
history.grid(row=5, column=0, columnspan=2, padx=10, pady=(0, 10), sticky="nsew")

def make_guess():
    global attempts, target
    val = entry.get().strip()
    if not val.isdigit():
        feedback.config(text="Enter a valid number")
        return
    num = int(val)
    if num < 1 or num > 50:
        feedback.config(text="Number must be 1–50")
        return
    attempts += 1
    if num < target:
        feedback.config(text="Too low")
        history.insert(tk.END, f"{num} - Too low")
    elif num > target:
        feedback.config(text="Too high")
        history.insert(tk.END, f"{num} - Too high")
    else:
        feedback.config(text=f"Correct! The number was {target}")
        history.insert(tk.END, f"{num} - Correct")
        guess_btn.config(state=tk.DISABLED)
    status.config(text=f"Attempts: {attempts}")
    entry.delete(0, tk.END)

def reset_game():
    global attempts, target
    target = random.randint(1, 50)
    attempts = 0
    feedback.config(text="")
    status.config(text="Attempts: 0")
    guess_btn.config(state=tk.NORMAL)
    entry.delete(0, tk.END)
    entry.focus_set()
    history.delete(0, tk.END)

guess_btn = tk.Button(root, text="Guess", font=("Arial", 14), command=make_guess)
guess_btn.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

reset_btn = tk.Button(root, text="New Game", font=("Arial", 12), command=reset_game)
reset_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(5, weight=1)

root.mainloop()
