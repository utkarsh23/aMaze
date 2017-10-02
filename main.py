import sys

from tkinterGui import displayMaze
from gridAttributes import Grid

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def main():
    errorTooManyArgs = "Too many command line arguments!\n----------\nTo learn usage:\n"
    errorTooManyArgs += "python main.py --help\n"
    errorTooManyArgs += "(or)\n"
    errorTooManyArgs += "python main.py -h\n"
    errorTooManyArgs += "----------"
    assert (len(sys.argv) < 3), errorTooManyArgs

    if len(sys.argv) == 2:
        if sys.argv[1] in ["--help", "-h"]:
            helpMessage = "\n----------\n"
            helpMessage += "$ python main.py\n"
            helpMessage += "Execution without any argument generates 10x10 random "
            helpMessage += "mazes in command line as well as GUI.\n"
            helpMessage += "----------\n"
            helpMessage += "$ python main.py <int>\n"
            helpMessage += "Execution with an argument specifying maze side dimension generates random mazes of that"
            helpMessage += " dimension on the command line only.\n"
            helpMessage += "----------\n"
            print(helpMessage)
            sys.exit(0)

        assert RepresentsInt(sys.argv[1]), "Side of a grid must be an integer value"
        maze = Grid(int(sys.argv[1]))
        print(maze)
        while True:
            option = input("Enter 1 to generate another random maze or 0 to exit: ")
            if option == "0":
                break
            elif option == "1":
                maze = Grid(int(sys.argv[1]))
                print(maze)
            else:
                print("Wrong input!")
    else:
        displayMaze()

if __name__ == '__main__':
    main()