import tkinter as tk
import random

root = tk.Tk()
root.title("Tic Tac Toe")

current = "X"
game_over = False
board = [""] * 9
buttons = []
vs_ai = False

status = tk.Label(root, text="Turn: X", font=("Arial", 16))
status.grid(row=3, column=0, columnspan=3, pady=(10, 5))

def check_winner():
    lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for a, b, c in lines:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a], (a, b, c)
    if all(board):
        return "Draw", None
    return None, None

def handle_click(i):
    global current, game_over
    if game_over or board[i]:
        return
    board[i] = current
    buttons[i].config(text=current)
    winner, line = check_winner()
    if winner == "Draw":
        status.config(text="Draw")
        game_over = True
        return
    if winner:
        for idx in line:
            buttons[idx].config(bg="#ffd54f")
        status.config(text=f"{winner} wins")
        game_over = True
        return
    current = "O" if current == "X" else "X"
    if vs_ai:
        ai_move()
    else:
        status.config(text=f"Turn: {current}")

def reset():
    global current, game_over, board
    current = "X"
    game_over = False
    board = [""] * 9
    for b in buttons:
        b.config(text="", bg="SystemButtonFace", state=tk.NORMAL)
    status.config(text="Turn: X")

def ai_move():
    global current, game_over
    if game_over:
        return
    if current != "O":
        status.config(text=f"Turn: {current}")
        return
    empty = [i for i, v in enumerate(board) if not v]
    if not empty:
        status.config(text="Draw")
        game_over = True
        return
    i = random.choice(empty)
    board[i] = current
    buttons[i].config(text=current)
    winner, line = check_winner()
    if winner == "Draw":
        status.config(text="Draw")
        game_over = True
        return
    if winner:
        for idx in line:
            buttons[idx].config(bg="#ffd54f")
        status.config(text=f"{winner} wins")
        game_over = True
        return
    current = "X"
    status.config(text=f"Turn: {current}")

for i in range(9):
    btn = tk.Button(root, text="", font=("Arial", 32), width=3, height=1, command=lambda i=i: handle_click(i))
    btn.grid(row=i // 3, column=i % 3, padx=5, pady=5, sticky="nsew")
    buttons.append(btn)

for r in range(3):
    root.grid_rowconfigure(r, weight=1)
for c in range(3):
    root.grid_columnconfigure(c, weight=1)

reset_btn = tk.Button(root, text="Reset", font=("Arial", 14), command=reset)
reset_btn.grid(row=4, column=0, columnspan=3, sticky="ew", padx=5, pady=5)

mode_pvp = tk.Button(root, text="1v1", font=("Arial", 14), command=lambda: set_mode(False))
mode_pvp.grid(row=5, column=0, columnspan=1, sticky="ew", padx=5, pady=5)
mode_pvc = tk.Button(root, text="1vComputer", font=("Arial", 14), command=lambda: set_mode(True))
mode_pvc.grid(row=5, column=1, columnspan=2, sticky="ew", padx=5, pady=5)

def set_mode(ai):
    global vs_ai
    vs_ai = ai
    reset()
    if vs_ai:
        status.config(text="Turn: X (1vComputer)")
    else:
        status.config(text="Turn: X (1v1)")

root.mainloop()
