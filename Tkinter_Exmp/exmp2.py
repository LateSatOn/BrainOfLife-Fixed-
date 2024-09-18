import tkinter as tk
import random

COLOR_MAP = {
    0: "white",
    1: "red",
    2: "green",
    3: "blue",
    4: "yellow"
}

grid_values = [
    [0, 1, 2, 3, 4],
    [1, 2, 3, 4, 0],
    [2, 3, 4, 0, 1],
    [3, 4, 0, 1, 2],
    [4, 0, 1, 2, 3]
]

rows = len(grid_values)
cols = len(grid_values[0])
cell_size = 50

is_randomizing = False
randomizing_time = 0

def draw_grid():
    canvas.delete("all")
    for row in range(rows):
        for col in range(cols):
            x1 = col * cell_size
            y1 = row * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            color = COLOR_MAP[grid_values[row][col]]
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

def randomize_grid():
    if is_randomizing:
        global grid_values, randomizing_time

        grid_values = [[random.randint(0, 4) for _ in range(cols)] for _ in range(rows)]

        draw_grid()
        randomizing_time += 1
        timer.config(text=f"Iteration  {randomizing_time}")

        root.after(1000, randomize_grid)

def toggle_randomization():
    global is_randomizing, randomizing_time

    is_randomizing = not is_randomizing

    if is_randomizing:
        randomizing_time = 0
        randomize_grid()

root = tk.Tk()
root.title("Colorful Grid with Randomization")

canvas = tk.Canvas(root, width=cols * cell_size, height=rows * cell_size)
canvas.pack()


draw_grid()

toggle_button = tk.Button(root, text="Start/Stop", command=toggle_randomization)
toggle_button.pack()

timer = tk.Label(root)
timer.place(relx=1.0, rely=1.0, anchor="se")

root.mainloop()