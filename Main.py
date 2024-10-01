import Logic as lc
import tkinter as tk
import MiscFun as mf

COLOR_MAP = {
    0: "white",
    1: "orange",
    2: "cyan",
    3: "indigo",
    4: "violet"
}

rows, cols = 19, 19
cell_list = []
mf.fill_cell_list(rows, cols, cell_list, 0, 0, 0)
mf.fill_cell_list_neighbors(rows, cols, cell_list, 'n')
mf.fill_cell_list_neighbors(rows, cols, cell_list, 't')

is_iterating = False
iteration = 0

def resize_grid(event=None):
    global cell_size

    window_width = root.winfo_width()
    window_height = root.winfo_height()

    cell_size = min(window_width // cols, (window_height - 150) // rows)

    canvas.config(width=cell_size * cols, height=cell_size * rows)

    draw_grid()

def draw_grid():
    canvas.delete("all")
    for row in range(rows):
        for col in range(cols):
            x1 = col * cell_size
            y1 = row * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size

            color = COLOR_MAP[cell_list[row][col].get_state()]

            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

            text_x = (x1 + x2) // 2
            text_y = (y1 + y2) // 2

            canvas.create_text(text_x, text_y, text=cell_list[row][col].get_signal(), fill="black")

def iterate_grid():
    global cell_list, iteration

    if is_iterating:

        for row in range(rows):
            for col in range(cols):
                lc.cell_logic(cell_list, row, col)

        for row in range(rows):
            for col in range(cols):
                if cell_list[row][col].get_enabled() > 0:
                    cell_list[row][col].change_enabled_by(-1)

        draw_grid()

        iteration += 1
        iteration_counter.config(text=f"Iteration  {iteration}")

        root.after(1000, iterate_grid)

def toggle_iteration():
    global is_iterating

    is_iterating = not is_iterating

    if is_iterating:
        iterate_grid()

def reset_iteration():
    global iteration
    iteration = 0
    iteration_counter.config(text=f"Iteration  {iteration}")

def on_canvas_click(event):
    if not is_iterating:
        col = event.x // cell_size
        row = event.y // cell_size

        if 0 <= col < cols and 0 <= row < rows:
            if cell_list[row][col].get_state() == 4:
                cell_list[row][col].set_state(0)
            else:
                cell_list[row][col].change_state_by(1)
            draw_grid()

root = tk.Tk()
root.title("Brain Of Life")
root.bind("<Configure>", resize_grid)
root.geometry("400x500")

canvas = tk.Canvas(root)
canvas.place(relx=0.5, rely=0.5, anchor="center")
canvas.bind("<Button-1>", on_canvas_click)

toggle_button = tk.Button(root, text="Start/Stop", command=toggle_iteration)
toggle_button.config(height=2, width=9)
toggle_button.place(relx=0.5, rely=1.0, anchor="s", x=-75, y=-15)

iteration_counter = tk.Button(root, text=f"Iteration  {iteration}", command=reset_iteration)
iteration_counter.config(height=2, width=9)
iteration_counter.place(relx=0.5, rely=1.0, anchor="s", x=75, y=-15)

resize_grid()

root.mainloop()
