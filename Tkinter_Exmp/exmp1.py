import tkinter as tk

root = tk.Tk()
root.title("My Game")
root.geometry("800x600")

count = 0

def on_button_click():
    global count
    count += 1
    label.config(text = f"You clicked the button {count} times!")

button = tk.Button(root, text = "Click Me", command = on_button_click)
button.pack()

label = tk.Label(root, text = "Click the button as manny times as possible!")
label.pack()

root.mainloop()
