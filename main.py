from graphics import Window, Line, Point
from cell import Cell


def main():
    win = Window(800, 600)
    line = Line(Point(0, 0), Point(500, 500))
    win.draw_line(line, "red")
    cell = Cell(win)
    cell.draw(100, 100, 500, 500)
    win.wait_for_close()


if __name__ == "__main__":
    main()
