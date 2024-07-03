from cell import Cell
from graphics import Window
from time import sleep


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Window,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells: list[list[Cell]] = []
        self._create_cells()

    def _create_cells(self) -> None:
        self._cells = [
            [Cell(self._win) for _ in range(self._num_cols)]
            for _ in range(self._num_rows)
        ]

        for j in range(self._num_rows):
            for i in range(self._num_cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        x1 = i * self._cell_size_x + self._x1
        y1 = j * self._cell_size_y + self._y1
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[j][i].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        self._win.redraw()
        sleep(0.1)
