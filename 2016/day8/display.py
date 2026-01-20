# display_main.py - created by ChatGPT
import tkinter as tk
from dataclasses import dataclass
from queue import Queue, Empty
from typing import Any, List, Optional, Callable

from display_renderer import GridRenderer

Grid = List[List[Any]]

@dataclass
class DisplayConfig:
    rows: int = 3
    cols: int = 7
    cell: int = 60
    title: str = "Grid Display"
    poll_ms: int = 16  # ~60 fps polling

class Display:
    def __init__(self, root: tk.Tk, config: DisplayConfig):
        self.root = root
        self.config = config

        self.root.title(config.title)

        self.canvas = tk.Canvas(root)
        self.canvas.pack()

        self.renderer = GridRenderer(
            canvas=self.canvas,
            rows=config.rows,
            cols=config.cols,
            cell=config.cell,
        )

        self._queue: "Queue[Optional[Grid]]" = Queue()
        self._last_grid: Optional[Grid] = None

        # Start polling for updates
        self._poll()

    def update(self, grid: Grid) -> None:
        # Thread-safe, just enqueue
        self._queue.put(grid)

    def close(self) -> None:
        # Signal close
        self._queue.put(None)

    def _poll(self) -> None:
        # Drain queue, keep only the latest grid for smooth rendering
        try:
            while True:
                item = self._queue.get_nowait()
                if item is None:
                    self.root.destroy()
                    return
                self._last_grid = item
        except Empty:
            pass

        if self._last_grid is not None:
            self.renderer.render(self._last_grid)

        self.root.after(self.config.poll_ms, self._poll)

def run_display(
    start_logic: Callable[[Display], None],
    config: Optional[DisplayConfig] = None
) -> None:
    """
    Creates the Tk window (main thread) and starts your logic in a background thread.
    Your logic receives a Display instance and can call display.update(grid) anytime.
    """
    import threading

    cfg = config or DisplayConfig()
    root = tk.Tk()
    display = Display(root, cfg)

    t = threading.Thread(target=start_logic, args=(display,), daemon=True)
    t.start()

    root.mainloop()
