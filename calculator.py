import tkinter as tk
from tkinter import ttk
import ast
import operator

root = tk.Tk()
root.title("Calculator")
root.geometry("360x520")

style = ttk.Style()
try:
    style.theme_use("clam")
except:
    pass
style.configure("Calc.TButton", font=("Segoe UI", 16), padding=8)
style.configure("Display.TEntry", padding=14)

display = tk.StringVar()
entry = ttk.Entry(root, textvariable=display, font=("Segoe UI", 22), justify="right", style="Display.TEntry")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=12, pady=12, ipady=8)

ops = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv, ast.Pow: operator.pow}

def safe_eval(expr):
    node = ast.parse(expr, mode="eval")
    def _eval(n):
        if isinstance(n, ast.Expression):
            return _eval(n.body)
        if isinstance(n, ast.UnaryOp) and isinstance(n.op, (ast.UAdd, ast.USub)):
            v = _eval(n.operand)
            return v if isinstance(n.op, ast.UAdd) else -v
        if isinstance(n, ast.BinOp) and type(n.op) in ops:
            left = _eval(n.left)
            right = _eval(n.right)
            return ops[type(n.op)](left, right)
        if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)):
            return n.value
        if isinstance(n, ast.Call) or isinstance(n, ast.Name):
            raise ValueError("invalid")
        if isinstance(n, ast.Subscript) or isinstance(n, ast.Attribute):
            raise ValueError("invalid")
        if isinstance(n, ast.Tuple) or isinstance(n, ast.List):
            raise ValueError("invalid")
        return 0
    return _eval(node)

def append(text):
    display.set(display.get() + text)

def clear():
    display.set("")

def back():
    s = display.get()
    display.set(s[:-1])

last_result = None

def equals():
    global last_result
    expr = display.get().strip()
    if not expr:
        return
    try:
        result = safe_eval(expr)
        last_result = result
        display.set(str(result))
    except Exception:
        display.set("Error")

def ans():
    if last_result is not None:
        append(str(last_result))

keys = [
    ("C", clear), ("⌫", back), ("(", lambda: append("(")), (")", lambda: append(")")),
    ("7", lambda: append("7")), ("8", lambda: append("8")), ("9", lambda: append("9")), ("÷", lambda: append("/")),
    ("4", lambda: append("4")), ("5", lambda: append("5")), ("6", lambda: append("6")), ("×", lambda: append("*")),
    ("1", lambda: append("1")), ("2", lambda: append("2")), ("3", lambda: append("3")), ("−", lambda: append("-")),
    ("0", lambda: append("0")), (".", lambda: append(".")), ("Ans", ans), ("+", lambda: append("+")),
]

r = 1
c = 0
for text, func in keys:
    b = ttk.Button(root, text=text, style="Calc.TButton", command=func)
    b.grid(row=r, column=c, sticky="nsew", padx=8, pady=8)
    c += 1
    if c == 4:
        c = 0
        r += 1

eq = ttk.Button(root, text="=", style="Calc.TButton", command=equals)
eq.grid(row=r, column=0, columnspan=4, sticky="nsew", padx=8, pady=8)

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(r + 1):
    root.grid_rowconfigure(i, weight=1)

def on_key(e):
    ch = e.char
    if ch in "0123456789.+-*/()":
        append(ch)
    elif e.keysym == "Return":
        equals()
    elif e.keysym == "Escape":
        clear()
    elif e.keysym == "BackSpace":
        back()

root.bind("<Key>", on_key)

root.mainloop()
