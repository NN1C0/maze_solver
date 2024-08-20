from classes.maze import Maze
from classes.window import Window
from classes.line import Line
from classes.point import Point
from classes.cell import Cell

def main():
    win = Window(800, 600)

    maze = Maze(5, 5, 18, 13, 20, 20, win)
    maze.solve()
    
    win.wait_for_close()



if __name__ == "__main__":
    main()