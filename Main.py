import API
import sys

def log(string):
    sys.stderr.write("{}\n".format(string))
    sys.stderr.flush()

def main():

    for i in range(API.mazeWidth()):
        for j in range(API.mazeHeight()):
            API.setText(i,j,"0")

    log("Started")
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

    direction = 0
    present = [0,0]
    past = [0,0]

    goals = [ [8,8], [8,7], [7,8], [7,7] ]
    directions = [ [0,1] ,[1,0],[0,-1],[-1,0] ]

    maze = [[ 0 for i in range(API.mazeHeight()) ] for j in range(API.mazeWidth())]

    def get_openings(position):
        openings = []
        for code,i in enumerate(directions):
            offset  = direction-code
            if abs(offset)==2:
                continue
            new_0 = position[0]+i[0]
            new_1 = position[1]+i[1]
            if(new_0 in range(0 , API.mazeWidth()) and new_1 in range(0, API.mazeHeight())) and maze[new_0][new_1]==0:
                if (offset==0 and not API.wallFront()) or (offset==-1 and not API.wallRight()) or (offset==1 and not API.wallLeft()):
                    openings.append([new_0, new_1])
                    continue
        return openings

    def move_to(from_position, to_position):
        nonlocal direction, present, past
        change = [to_position[0]-from_position[0],to_position[1]-from_position[1]]
        new_direction = directions.index(change)
        log(new_direction)

        offset = ((new_direction - direction)+4)%4
        log(offset)
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
        if False:
            sys.exit()
        pass

    def traverse(position):
        check(position)
        openings = get_openings(position)
        log(openings)
        if openings == [] :
            return
        for i in openings:
            log("traversing from "+str(position)+" to "+str(i))
            move_to(position,i)
            traverse(i)
            log("traversing from "+str(i)+" to "+str(position))
            move_to(i,position)

    traverse([0,0])
    log("Ended")
  
if __name__ == "__main__":
    main()
