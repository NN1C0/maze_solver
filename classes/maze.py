import random
from classes.cell import Cell
from classes.point import Point
from time import sleep

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win = None,
            seed = None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._seed = random.seed(seed)

        self._cells = [] #col, rows

        self._create_cells()
        self._break_entrance_and_walls()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
    
    def solve(self):
        return self._solve_r(0,0)

    def _solve_r(self, i, j):
        print(i, j)
        self._animate(0.05)
        self._cells[i][j].visited = True

        if i == self.num_cols - 1 and j == self.num_rows - 1:
            print('end')
            return True
        
        if (
            j - 1 > 0
            and self._cells[i][j - 1].visited == False 
            and not self._cells[i][j].has_left_wall
        ):
                self._cells[i][j].draw_move(self._cells[i][j - 1])
                if self._solve_r(i, j - 1):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i][j - 1], True)
                
        if (
             i + 1 < self.num_cols
             and self._cells[i + 1][j].visited == False
             and not self._cells[i][j].has_down_wall
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        if (
            j + 1 < self.num_rows
            and self._cells[i][j + 1].visited == False 
            and not self._cells[i][j].has_right_wall
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        if (
            i - 1 > 0
            and self._cells[i - 1][j].visited == False 
            and not self._cells[i][j].has_up_wall
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        print('nothing')
        return False


    def _create_cells(self):
        for y in range(self.y1, self.y1 + (self.num_cols * self.cell_size_x), self.cell_size_x):
            col = []
            for x in range(self.x1 , self.x1 + (self.num_rows * self.cell_size_y), self.cell_size_y):
                col.append(Cell(Point(x, y), self.win, self.cell_size_x, self.cell_size_y))


            self._cells.append(col)
        
        if self.win:
            for i in range(len(self._cells)):
                for j in range(len(self._cells[i])):
                    self._draw_cell(i, j)

    def _break_entrance_and_walls(self):
        self._cells[0][0].has_left_wall = False
        self._draw_cell(0,0)

        self._cells[-1][-1].has_right_wall = False
        self._draw_cell(-1, -1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while(True):
            need_to_visit = []
            if j - 1 > 0:
                if self._cells[i][j - 1].visited == False:
                    need_to_visit.append((i, j - 1))
            if i + 1 <= self.num_cols - 1:
                if self._cells[i + 1][j].visited == False:
                    need_to_visit.append((i + 1, j))
            if j + 1 <= self.num_rows - 1:
                if self._cells[i][j + 1].visited == False:
                    need_to_visit.append((i, j + 1))
            if i - 1 > 0:
                if self._cells[i - 1][j].visited == False:
                    need_to_visit.append((i - 1, j))

            if len(need_to_visit) == 0:
                return

            next_cell = need_to_visit[random.randrange(0, len(need_to_visit))]
            self._cells[i][j].break_walls_to_cell(self._cells[next_cell[0]][next_cell[1]])
            self._animate()

            self._break_walls_r(next_cell[0], next_cell[1])
    
    def _reset_cells_visited(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._cells[i][j].visited = False
    
    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate()

    def _animate(self, time=0.02):
        if self.win:
            self.win.redraw()
            sleep(time)