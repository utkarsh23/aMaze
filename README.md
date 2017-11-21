# aMaze
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

aMaze is a Maze Generator that implements a backtracking algorithm and uses stacks to generate random mazes. This project uses python's Tkinter Toolkit to display the maze in a GUI.

## How to run this project

```
git clone https://github.com/utkarsh23/aMaze.git
cd aMaze
python3 main.py --help
```

## Algorithm
1) Select the starting cell for the maze.
2) Randomly select any adjacent cell that has not been visited, remove the wall between these two cells and move to the selected adjacent cell. On moving to this new cell, add it to a stack.
3) If all adjcent cells have been visited, use the stack to backtrack to the last cell that has unvisited adjacent cells and pop the cells as you backtrack to previously visited cells. Then repeat step 2.
4) The algorithm ends when all cells have been visited.
