import sys
import time
maze = [
    [1,1,1,1,1,1,1,1,1,1,1,2,1,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,0,1],
    [1,1,1,1,1,0,1,0,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,0,1,0,0,0,0,1],
    [1,0,1,1,1,0,0,0,0,0,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

def showmaze():
    print()
    for row in maze:
        for item in row:
            print(item, end="")
        print()

def action(x,y):
    time.sleep(1)
    if maze[y][x] == 2:
        print("Finished")
        sys.exit()
    if maze[y][x] == 0:
        maze[y][x] = '*'
        AI(x,y)

def AI(x,y):
    showmaze()
    action(x+1,y)
    action(x-1,y)
    action(x,y+1)
    action(x,y-1)

AI(1,1)

