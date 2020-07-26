import API
import sys

def log(string):
    sys.stderr.write("{}\n".format(string))
    sys.stderr.flush()

def main():

    for i in range(API.mazeWidth()):
        for j in range(API.mazeHeight()):
            API.setText(i,j,"0")

    log("Running...")
    API.setColor(0, 0, "G")
    API.setText(0, 0, "Start")
    API.setColor(8, 8, "C")
    API.setText(8, 8, "Fin")
    API.setColor(7, 8, "C")
    API.setText(7, 8, "Fin")
    API.setColor(8, 7, "C")
    API.setText(8, 7, "Fin")
    API.setColor(7, 7, "C")
    API.setText(7, 7, "Fin")

    present_position = [0,0]
    present_direction = 0
    prev_position = [0,0]

    goals = [ [8,8], [8,7], [7,8], [7,7] ]
    directions = [ [0,1],[1,0],[0,-1],[-1,0] ]

    maze = [[ 0 for i in range(API.mazeHeight()) ] for j in range(API.mazeWidth())]

    def one_step_position(position, direction):
        pass

    while True:

        if API.wallFront() and API.wallRight() and API.wallLeft():
            API.turnLeft()
            API.turnLeft()
            present_direction = (present_direction+2)%4
            API.setColor(*present_position, "R")
            API.setText(*present_position, "-1")
            maze[present_position[0]][present_position[1]] = -1

        if API.wallLeft() and API.wallRight() and maze[prev_position[0]][prev_position[1]]==-1:
            API.setColor(*present_position, "R")
            API.setText(*present_position, "-1")
            maze[present_position[0]][present_position[1]] = -1

        if not API.wallLeft():
            API.turnLeft()
            present_direction = (present_direction+3)%4

        while API.wallFront():
            API.turnRight()
            present_direction = (present_direction+1)%4
        
        API.moveForward()
        prev_position = present_position.copy()
        present_position[0] += directions[present_direction][0]
        present_position[1] += directions[present_direction][1]
        if present_position in goals:
            break

if __name__ == "__main__":
    main()
