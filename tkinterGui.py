from tkinter import *
from gridAttributes import  Grid

def displayMaze():

    maze = Grid()
    print(maze) #To print maze in command line

    gui = Tk()
    gui.title("aMaze Maze Generator")

    canvas = Canvas(gui, width=600, height=550)
    canvas.pack()
    border = canvas.create_rectangle(100, 100, 500, 500, width=2)
    xTrackerHorizontal = 100
    yTrackerHorizontal = 140
    xTrackerVertical = 140
    yTrackerVertical = 100
    for k in range(maze.side ** 2):
        if maze.cells[k].firstCell:
            # Red cross is starting cell in the maze
            canvas.create_line(
                xTrackerVertical - 10,
                yTrackerVertical + 10,
                xTrackerVertical - 30,
                yTrackerVertical + 30,
                fill="red",
                width=2
            )
            canvas.create_line(
                xTrackerVertical- 30,
                yTrackerVertical + 10,
                xTrackerVertical - 10,
                yTrackerVertical + 30,
                fill="red",
                width=2
            )
        if maze.cells[k].lastCell:
            # Green cross is last cell in the maze
            canvas.create_line(
                xTrackerVertical - 10,
                yTrackerVertical + 10,
                xTrackerVertical - 30,
                yTrackerVertical + 30,
                fill="green",
                width=2
            )
            canvas.create_line(
                xTrackerVertical- 30,
                yTrackerVertical + 10,
                xTrackerVertical - 10,
                yTrackerVertical + 30,
                fill="green",
                width=2
            )
        if maze.cells[k].S:
            canvas.create_line(
                xTrackerHorizontal,
                yTrackerHorizontal,
                xTrackerHorizontal + 40,
                yTrackerHorizontal,
                width=2
            )
        xTrackerHorizontal += 40
        if xTrackerHorizontal == 500:
            xTrackerHorizontal = 100
            yTrackerHorizontal += 40

        if maze.cells[k].E:
            canvas.create_line(
                xTrackerVertical,
                yTrackerVertical,
                xTrackerVertical,
                yTrackerVertical + 40,
                width=2
            )
        if xTrackerVertical == 500:
            xTrackerVertical = 100
            yTrackerVertical += 40
        xTrackerVertical += 40

    randomizeMazeBtn = Button(text="Randomize", command=lambda: generateNewMaze(gui))
    randomizeMazeBtn.pack()

    gui.mainloop()

def generateNewMaze(gui):
    gui.destroy()
    displayMaze()