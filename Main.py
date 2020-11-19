import API
import sys
import time

def log(string):
    sys.stderr.write("{}\n".format(string))
    sys.stderr.flush()

mappings = {}
current_direction = 0
x = 0
y = 0
steps = 0

direction_to_move = {
        (0,-1)  : 2,
        (0,1)   : 0,
        (1,0)   : 1,
        (-1,0)  : 3
        }

direction_to_move_inverse = {
        2 : (0,-1),
        0 : (0,1),
        1 : (1,0),
        3 : (-1,0)
        }

# Node to solve in the shortest path algorithm 
class Node():

    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.visited = False
        self.isEnd = False
        self.neighbours = set({})
        self.pos = (self.x,self.y)
        self.processed = False

    def n_neighbours(self):
        return len(self.children)

# CONNECT 2 NODES
def connect(node1, node2):
    node1.neighbours.add(node2)
    node2.neighbours.add(node1)


# MOVE API FROM SOURCE POSITION TO DESTINATION POSITION
def apiMove(source, destination):
    global current_direction,steps
    steps += 1
    dx = destination.x - source.x
    dy = destination.y - source.y
    future_direction = direction_to_move[(dx,dy)]

    diff = future_direction-current_direction
    if(diff==1 or diff==-3):
        API.turnRight()
    if(diff==2 or diff==-2):
        API.turnLeft()
        API.turnLeft()
    if(diff==3 or diff==-1):
        API.turnLeft()
    API.moveForward()
    current_direction = future_direction


# USE CURRENT DIRECTION AND LOCAL ADVANCEMENT DIRECTION TO GET FUTURE POSITION
def directionMapper(direction_character):
    global current_direction
    d_num = 0
    if(direction_character=='L'):
        d_num = -1
    elif(direction_character=='R'):
        d_num = 1
    elif(direction_character=='D'):
        d_num = 2
    global_direction = (current_direction+d_num+4)%4
    changes = direction_to_move_inverse[global_direction]
    return (x+changes[0], y+changes[1])


# SCAN THE NEIGHBOURS OF A NODE
def scan(node):
    # order = [3,2,1]
    # order = [1,2,3]
    # order = [2,1,3]
    order = [2,3,1]

    for i in order:
        if i==1:
            if not API.wallLeft():
                predicted_pos = directionMapper('L')
                node2 = None
                try : 
                    node2  = mappings[predicted_pos]
                except:
                    mappings[predicted_pos] = Node(*predicted_pos)
                    node2  = mappings[predicted_pos]
                connect(node, node2)
        if i==2:
            if not API.wallFront():
                predicted_pos = directionMapper('U')
                node2 = None
                try : 
                    node2  = mappings[predicted_pos]
                except:
                    mappings[predicted_pos] = Node(*predicted_pos)
                    node2  = mappings[predicted_pos]
                connect(node, node2)
        if i==3:
            if not API.wallRight():
                predicted_pos = directionMapper('R')
                node2 = None
                try : 
                    node2  = mappings[predicted_pos]
                except:
                    mappings[predicted_pos] = Node(*predicted_pos)
                    node2  = mappings[predicted_pos]
                connect(node, node2)

# MAIN FLOODFILL
def floodfill(node):
    global x,y
    scan(node)
    node.processed = True
    API.setColor(*node.pos, "r")
    for i in node.neighbours :
        if not i.processed:
            apiMove(node, i)
            x,y = i.x, i.y
            floodfill(i)
            apiMove(i, node)
            x,y = node.x, node.y

def main():
    head = Node(0,0)
    floodfill(head)
    log("Steps : "+str(steps));
    
if __name__ == "__main__":
    main()
