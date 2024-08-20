from classes.point import Point
from classes.window import Window
from classes.line import Line

class Cell():

    def __init__(self, spawn_point: Point, window: Window = None, cell_width: int = 40, cell_height: int = 40):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_up_wall = True
        self.has_down_wall = True
        self.x1 = spawn_point.x
        self.y1 = spawn_point.y
        self.x2 = spawn_point.x + cell_width
        self.y2 = spawn_point.y + cell_height
        self.middle = Point(self.x1 + (cell_width / 2), self.y1 + (cell_height / 2))
        self.__window = window

        self.visited = False

    def draw(self):
        if self.__window:
            if self.has_up_wall:
                self.__window.draw_line(Line(Point(self.x1, self.y1), Point(self.x2, self.y1)), "black")
            elif not self.has_up_wall:
                self.__window.draw_line(Line(Point(self.x1, self.y1), Point(self.x2, self.y1)), "white")
            
            if self.has_right_wall:
                self.__window.draw_line(Line(Point(self.x2, self.y1), Point(self.x2, self.y2)), "black")
            elif not self.has_right_wall:
                self.__window.draw_line(Line(Point(self.x2, self.y1), Point(self.x2, self.y2)), "white")

            if self.has_down_wall:
                self.__window.draw_line(Line(Point(self.x2, self.y2), Point(self.x1, self.y2)), "black")
            elif not self.has_down_wall:
                self.__window.draw_line(Line(Point(self.x2, self.y2), Point(self.x1, self.y2)), "white")
            
            if self.has_left_wall:
                self.__window.draw_line(Line(Point(self.x1, self.y2), Point(self.x1, self.y1)), "black")
            elif not self.has_left_wall:
                self.__window.draw_line(Line(Point(self.x1, self.y2), Point(self.x1, self.y1)), "white")

    def draw_move(self, to_cell, undo=False):
        line_color = "white" if undo else "red"
        connecting_line = Line(self.middle, to_cell.middle)

        #self.break_walls_to_cell(to_cell)
        
        connecting_line.draw(self.__window.canvas, line_color)

    def break_walls_to_cell(self, to_cell):
        if self.x1 < to_cell.x1:
            self.has_right_wall = False
            to_cell.has_left_wall = False
        if self.x1 > to_cell.x1:
            self.has_left_wall = False
            to_cell.has_right_wall = False
        if self.y1 < to_cell.y1:
            self.has_down_wall = False
            to_cell.has_up_wall = False
        if self.y1 > to_cell.y1:
            self.has_up_wall = False
            to_cell.has_down_wall = False

        self.draw()
        to_cell.draw()