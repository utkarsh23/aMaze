from tkinter import *

def displayMaze(maze):
    gui = Tk()
    canvas = Canvas(gui, width=600, height=600)
    canvas.pack()

    border = canvas.create_rectangle(100, 100, 500, 500)
    horizontalLines = [None for i in range(maze.side ** 2)]
    verticalLines = [None for j in range(maze.side ** 2)]
    xTrackerHorizontal = 100
    yTrackerHorizontal = 140
    xTrackerVertical = 140
    yTrackerVertical = 100
    for k in range(maze.side ** 2):
        if maze.cells[k].S:
            horizontalLines[k] = canvas.create_line(
                xTrackerHorizontal,
                yTrackerHorizontal,
                xTrackerHorizontal + 40,
                yTrackerHorizontal
            )
        xTrackerHorizontal += 40
        if xTrackerHorizontal == 500:
            xTrackerHorizontal = 100
            yTrackerHorizontal += 40

        if maze.cells[k].E:
            verticalLines[k] = canvas.create_line(
                xTrackerVertical,
                yTrackerVertical,
                xTrackerVertical,
                yTrackerVertical + 40
            )
        if xTrackerVertical == 500:
            xTrackerVertical = 100
            yTrackerVertical += 40
        xTrackerVertical += 40

    gui.mainloop()