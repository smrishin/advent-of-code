# renderer.py - created by ChatGPT
import tkinter as tk
from typing import List, Any

Grid = List[List[Any]]  # you can use 0/1, ".", "#", etc.

class GridRenderer:
    def __init__(
        self,
        canvas: tk.Canvas,
        rows: int,
        cols: int,
        cell: int = 60,
        bg: str = "black",
        outline: str = "gray60",
        off_color: str = "gray25",
        on_color: str = "lime green",
    ):
        self.canvas = canvas
        self.rows = rows
        self.cols = cols
        self.cell = cell
        self.off_color = off_color
        self.on_color = on_color

        self.canvas.configure(
            width=cols * cell,
            height=rows * cell,
            bg=bg,
            highlightthickness=0,
        )

        self.rects: List[List[int]] = []
        for r in range(rows):
            row_rects: List[int] = []
            for c in range(cols):
                x1 = c * cell
                y1 = r * cell
                x2 = x1 + cell
                y2 = y1 + cell
                rect_id = self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=off_color,
                    outline=outline,
                )
                row_rects.append(rect_id)
            self.rects.append(row_rects)

    def render(self, grid: Grid) -> None:
        # Treat truthy as "on". If you use "." / "#", this still works if you map later.
        for r in range(self.rows):
            for c in range(self.cols):
                val = grid[r][c]
                is_on = (val == "#") or (val == 1) or (val is True)
                color = self.on_color if is_on else self.off_color
                self.canvas.itemconfig(self.rects[r][c], fill=color)

        self.canvas.update_idletasks()
