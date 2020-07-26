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


    def next_position(position, direction):
        return [position[0]+directions[direction][0],position[1]+directions[direction][1]]


    def move(position, direction):
        position[0] += directions[direction][0]
        position[1] += directions[direction][1]
        return position


    def get_value(position):
        return maze[position[0]][position[1]]


    def set_value(position, direction):
        nonlocal maze
        maze[position[0]][position[1]] = -1

    def is_blocked(position):
        block_count = 0
        if API.wallFront():
            block_count += 1
        if API.wallRight():
            block_count += 1
        if API.wallLeft():
            block_count += 1
        if get_value(prev_position) == -1:
            block_count += 1

        if block_count == 4 :
            log("Error :  Full Block")
        if block_count >= 3 :
            return True

    def get_available_directions(position):
        available_directions = []
        for direction in range(4):
            if not is_blocked(move(position,direction)):
                available_directions.append(direction)
        return available_directions

    def Mouse():

        nonlocal maze, present_position, present_direction, prev_position

        if API.wallFront() and API.wallRight() and API.wallLeft():   # turn back
            API.turnLeft()
            API.turnLeft()
            present_direction = (present_direction+2)%4
            set_value(present_position, -1)
            
            API.setColor(*present_position, "R")
            API.setText(*present_position, "-1")


        if is_blocked(present_position):
            set_value(present_position, -1)

            API.setColor(*present_position, "R")
            API.setText(*present_position, "-1")


        if not API.wallLeft():
            API.turnLeft()
            present_direction = (present_direction+3)%4


        while API.wallFront():
            API.turnRight()
            present_direction = (present_direction+1)%4


        API.moveForward()
        prev_position = present_position.copy()
        present_position = move(present_position, present_direction)
        if present_position in goals:
            return
        Mouse()

    Mouse()

if __name__ == "__main__":
    main()
