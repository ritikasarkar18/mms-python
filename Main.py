import API
import sys
import time

def log(string):
    sys.stderr.write("{}\n".format(string))
    sys.stderr.flush()

def main():

    def fill_maze():
        for i in range(API.mazeWidth()):
            for j in range(API.mazeHeight()):
                API.setText(i,j,"0")

        log("Scanning")
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

    REVERSE_OPENINGS = True    #True for right priority, False for left
    direction = 0
    present = [0,0]
    past = [0,0]

    goals = [ [8,8], [8,7], [7,8], [7,7] ]
    directions = [ [0,1] ,[1,0],[0,-1],[-1,0] ]

    maze = [[ 0 for i in range(API.mazeHeight()) ] for j in range(API.mazeWidth())]

    def set_value(position, value):
        maze[position[0]][position[1]] = value
        API.setText(*position, str(value))
        if value==-1:
            API.setColor(*position, "R")
        else:
            API.setColor(*position, "Y")

    def get_value(position):
        return maze[position[0]][position[1]]

    def get_openings(position):
        openings = []
        for code,i in enumerate(directions):
            offset  = ((direction-code)+4)%4
            if abs(offset)==2:
                continue
            new_0 = position[0]+i[0]
            new_1 = position[1]+i[1]
            if(new_0 in range(0 , API.mazeWidth()) and new_1 in range(0, API.mazeHeight())) and maze[new_0][new_1]!=-1:
                if (offset==0 and not API.wallFront()) or (offset==3 and not API.wallRight()) or (offset==1 and not API.wallLeft()):
                    openings.append(([new_0, new_1],code))
                    continue
        if REVERSE_OPENINGS :
            openings = openings[::-1]
        return openings

    def move_to(from_position, to_position, direct=-1):
        nonlocal direction, present, past
        if direct==-1:
            change = [to_position[0]-from_position[0],to_position[1]-from_position[1]]
            new_direction = directions.index(change)
        else :
            new_direction = direct

        offset = ((new_direction - direction)+4)%4
        if offset==1:
            API.turnRight()
        elif offset==3:
            API.turnLeft()
        elif abs(offset)==2:
            API.turnLeft()
            API.turnLeft()

        API.moveForward()
        direction = new_direction
        past = from_position.copy()
        present = to_position.copy()

    def check(position):
        if position in goals :
            return True
        if False:
            sys.exit()
    
    #####    GET PATH    #####
    def traverse(position,value):
        end  = check(position)
        if end:
            return 0
        if get_value(position)==-1:
            return -1
        values = []
        set_value(position, -1)
        openings = get_openings(position)
        if openings == [] :
            set_value(position, -1)
            return -1
        for i in openings:
            move_to(position,i[0],i[1])
            values.append(traverse(i[0], value+1))
            move_to(i[0],position)
        values = [i for i in values if i>=0]
        if values==[]:
            set_value(position, -1)
            return -1
        else:
            set_value(position, min(values))
            return min(values)+1
    
    fill_maze()
    traverse([0,0], 0)
    log("Scanning ended")

    #####    PROPER RUN    #####

    API.turnLeft()
    API.turnLeft()
    direction = 0

    log('Ready for good run!')
    time.sleep(3)
    steps_taken = 0

    def fresh_run(position):
        nonlocal steps_taken
        steps_taken += 1
        if check(position):
            return
        openings = get_openings(position)
        move_to(position, openings[0][0])
        fresh_run(openings[0][0])
        move_to(openings[0][0], position)

    fresh_run([0,0])
    
    log('I am back')
    log("Steps taken : "+str(steps_taken))
  
if __name__ == "__main__":
    main()
