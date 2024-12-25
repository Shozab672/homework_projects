import tkinter as tk
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20


def erase_objects(canvas, eraser, cells):
    """Erase objects in contact with the eraser"""
    eraser_coords = canvas.coords(eraser)

    for cell in cells:
        cell_coords = canvas.coords(cell)
        # Check for overlap
        if (
            eraser_coords[2] > cell_coords[0] and
            eraser_coords[0] < cell_coords[2] and
            eraser_coords[3] > cell_coords[1] and
            eraser_coords[1] < cell_coords[3]
        ):
            canvas.itemconfig(cell, fill="white")  # Set the cell to white


def main():
    root = tk.Tk()
    root.title("Eraser Canvas")

    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
    canvas.pack()

    # Create the grid of blue cells
    cells = []
    for row in range(CANVAS_HEIGHT // CELL_SIZE):
        for col in range(CANVAS_WIDTH // CELL_SIZE):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE
            cell = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill="blue", outline="black")
            cells.append(cell)

    # Create the eraser
    eraser = canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="pink", outline="black")

    def move_eraser(event):
        """Move the eraser and erase overlapping cells"""
        canvas.coords(eraser, event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE)
        erase_objects(canvas, eraser, cells)

    # Bind the mouse motion to move the eraser
    canvas.bind("<Motion>", move_eraser)

    root.mainloop()


if __name__ == "__main__":
    main()
