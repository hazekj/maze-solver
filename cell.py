from graphics import Line, Point


class Cell:
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = window

    def draw(self, x1: int, y1: int, x2: int, y2: int):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)

    def draw_move(self, to_cell, undo=False):
        mid_xS = (self._x1 + self._x2) // 2
        mid_yS = (self._y1 + self._y2) // 2
        mid_xC = (to_cell._x1 + to_cell._x2) // 2
        mid_yC = (to_cell._y1 + to_cell._y2) // 2
        line = Line(Point(mid_xS, mid_yS), Point(mid_xC, mid_yC))
        color = "gray"
        if undo:
            color = "red"
        self._win.draw_line(line, color)

        # line = Line(Point(self.))
