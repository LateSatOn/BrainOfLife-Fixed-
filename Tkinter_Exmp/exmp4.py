import tkinter as tk
import random

COLOR_MAP = {
    0: "white",
    1: "orange",
    2: "cyan",
    3: "indigo",
    4: "violet"
}

rows, cols = 17, 17
grid_values = [[0 for _ in range(cols)] for _ in range(rows)]
cell_size = 30

is_iterating = False
iteration = 0

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

def iteratate_grid():
    if is_iterating:
        global grid_values, iteration

        for row in range(rows):
            for col in range(cols):
                #Logic here

        draw_grid()
        iteration += 1
        timer.config(text=f"Iteration  {iteration}")

        root.after(1000, iteratate_grid)

def toggle_iteration():
    global is_iterating, iteration

    is_iterating = not is_iterating

    if is_iterating:
        randomizing_time = 0
        iteratate_grid()

def on_canvas_click(event):
    if is_iterating == False:
        col = event.x // cell_size
        row = event.y // cell_size

        if 0 <= col < cols and 0 <= row < rows:
            grid_values[row][col] = (grid_values[row][col] + 1) % 5
            draw_grid()

root = tk.Tk()
root.title("Colorful Grid with Randomization")

canvas = tk.Canvas(root, width=cols * cell_size, height=rows * cell_size)
canvas.pack()

canvas.bind("<Button-1>", on_canvas_click)

draw_grid()

toggle_button = tk.Button(root, text="Start/Stop", command=toggle_iteration)
toggle_button.pack()

timer = tk.Label(root)
timer.place(relx=1.0, rely=1.0, anchor="se")

root.mainloop()