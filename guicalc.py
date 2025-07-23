import tkinter as tk

is_dark_mode = True

# Theme settings
themes = {
    "dark": {
        "bg": "#1e1e1e", "fg": "white",
        "entry_bg": "#2e2e2e", "btn_bg": "#3c3c3c", "active_bg": "#5e5e5e"
    },
    "light": {
        "bg": "#ffffff", "fg": "black",
        "entry_bg": "#f0f0f0", "btn_bg": "#dddddd", "active_bg": "#bbbbbb"
    }
}

def apply_theme():
    theme = themes["dark"] if is_dark_mode else themes["light"]
    root.config(bg=theme["bg"])
    entry.config(bg=theme["entry_bg"], fg=theme["fg"], insertbackground=theme["fg"])
    toggle_btn.config(bg=theme["btn_bg"], fg=theme["fg"])
    for frame in button_frames:
        frame.config(bg=theme["bg"])
        for btn in frame.winfo_children():
            btn.config(bg=theme["btn_bg"], fg=theme["fg"], activebackground=theme["active_bg"])

def toggle_theme():
    global is_dark_mode
    is_dark_mode = not is_dark_mode
    toggle_btn.config(text="☀️" if is_dark_mode else "🌙")
    apply_theme()

def animate_button(btn):
    theme = themes["dark"] if is_dark_mode else themes["light"]
    btn.config(bg=theme["active_bg"])
    btn.after(150, lambda: btn.config(bg=theme["btn_bg"]))  # restore after 150ms

def on_click(event):
    button_text = event.widget["text"]
    animate_button(event.widget)
    if button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

def on_key(event):
    key = event.char
    if key in '0123456789+-*/.':
        entry.insert(tk.END, key)
    elif event.keysym == 'Return':
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif event.keysym == 'BackSpace':
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current[:-1])

root = tk.Tk()
root.title("Animated Calculator")
root.geometry("320x470")
root.resizable(False, False)

# Toggle button
toggle_btn = tk.Button(root, text="🌙", font=("Arial", 12), command=toggle_theme)
toggle_btn.pack(anchor="ne", padx=10, pady=5)

# Entry field
entry = tk.Entry(root, font=("Arial", 20), borderwidth=0)
entry.pack(fill=tk.BOTH, ipadx=8, ipady=15, padx=10, pady=10)
entry.focus()

# Buttons
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

button_frames = []
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both", padx=5)
    button_frames.append(frame)
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font=("Arial", 18), relief=tk.FLAT, borderwidth=0)
        btn.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        btn.bind("<Button-1>", on_click)

root.bind("<Key>", on_key)

apply_theme()
root.mainloop()

