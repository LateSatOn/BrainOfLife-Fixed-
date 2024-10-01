import Logic as lC  # Imports logic functions
import MiscFun as mF  # Imports utility functions
import tkinter as tk  # GUI framework

# Maps cell state values to colors
COLOR_MAP = {
    0: "white",
    1: "orange",
    2: "cyan",
    3: "indigo",
    4: "violet"
}

# Grid settings
rows, cols = 19, 19
cell_list = []  # Holds all cells
mF.fill_cell_list(rows, cols, cell_list, 0, 0, 0)  # Initialize cell objects
mF.fill_cell_list_neighbors(rows, cols, cell_list, 't')  # Set transmitters neighbors for cell objects
mF.fill_cell_list_neighbors(rows, cols, cell_list, 'n')  # Set neurons neighbors for cell objects

is_iterating = False  # Tracks iteration state
iteration = 0  # Iteration counter

# Adjusts grid size when window is resized
def resize_grid(event=None):
    global cell_size
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    # Set cell size based on window dimensions
    cell_size = min(window_width // cols, (window_height - 150) // rows)
    # Resize canvas and redraw grid
    canvas.config(width=cell_size * cols, height=cell_size * rows)
    draw_grid()

# Draws grid on canvas
def draw_grid():
    canvas.delete("all")  # Clear previous grid
    for row in range(rows):
        for col in range(cols):
            # Calculate cell coordinates
            x1, y1 = col * cell_size, row * cell_size
            x2, y2 = x1 + cell_size, y1 + cell_size
            # Set cell color based on state
            color = COLOR_MAP[cell_list[row][col].get_state()]
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
            # Display cell signal in the center of the cell
            canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=cell_list[row][col].get_signal(), fill="black")

# Logic iteration on each cell
def iterate_grid():
    global iteration
    if is_iterating:
        # Apply logic to all cells
        for row in range(rows):
            for col in range(cols):
                lC.cell_logic(cell_list, row, col)
        # Reset enabled status after logic
        for row in range(rows):
            for col in range(cols):
                if cell_list[row][col].get_disabled() > 0:
                    cell_list[row][col].change_disabled_by(-1)

        draw_grid()  # Redraw grid
        iteration += 1  # Increment iteration counter
        iteration_counter.config(text=f"Iteration {iteration}")
        root.after(1000, iterate_grid)  # Repeat after 1 second

# Toggles between start/stop states for iteration
def toggle_iteration():
    global is_iterating
    is_iterating = not is_iterating
    if is_iterating:
        iterate_grid()

# Resets iteration counter
def reset_iteration():
    global iteration
    iteration = 0
    iteration_counter.config(text=f"Iteration {iteration}")

# Handles clicks on the grid and changes cell states
def on_canvas_click(event):
    if not is_iterating:
        # Calculate clicked cell
        col = event.x // cell_size
        row = event.y // cell_size
        # Ensure within grid bounds and cycle through states
        if 0 <= col < cols and 0 <= row < rows:
            if cell_list[row][col].get_state() == 4:
                cell_list[row][col].set_state(0)
            else:
                cell_list[row][col].change_state_by(1)
            draw_grid()  # Redraw grid

# Set up the main window
root = tk.Tk()
root.title("Brain Of Life")
root.bind("<Configure>", resize_grid)  # Bind window resize event
root.geometry("400x500")

# Create canvas for the grid
canvas = tk.Canvas(root)
canvas.place(relx=0.5, rely=0.5, anchor="center")
canvas.bind("<Button-1>", on_canvas_click)  # Bind left-click event

# Start/Stop button for iteration
toggle_button = tk.Button(root, text="Start/Stop", command=toggle_iteration)
toggle_button.config(height=2, width=9)
toggle_button.place(relx=0.5, rely=1.0, anchor="s", x=-75, y=-15)

# Iteration counter button
iteration_counter = tk.Button(root, text=f"Iteration {iteration}", command=reset_iteration)
iteration_counter.config(height=2, width=9)
iteration_counter.place(relx=0.5, rely=1.0, anchor="s", x=75, y=-15)

resize_grid()  # Initialize grid size
root.mainloop()  # Start the GUI event loop
