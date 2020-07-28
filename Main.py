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
    directions = [ [0,1],[1,0],[0,-1],[-1,0] ]

    maze = [[ 0 for i in range(API.mazeHeight()) ] for j in range(API.mazeWidth())]

    def get_openings(position):
        pass

    def move_to(past, future):
        pass

    def check(position):
        if False:
            sys.exit()
        pass

    def traverse(position):
        check(position)
        openings = get_openings(position)
        if openings == [] :
            return
        for i in get_openings:
            move_to(i)
            traverse(i)
            move_to(position)

    log("Ended")
  
if __name__ == "__main__":
    main()
