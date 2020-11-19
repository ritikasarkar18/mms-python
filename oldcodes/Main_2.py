import API
import sys
import time

mouse = None
manager = None  

# Node to solve in the shortest path algorithm 
class Node():

    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.visited = False
        self.isEnd = False
        self.children = {}
        self.pos = (self.x,self.y)

    def n_neighbours(self):
        return len(self.children)


# Manager will facilitate fuctionalities and conversions related to the maze
class MazeManager():

    def __init__(self):
        self.mapping = {}                           # stores a map to (x,y) => Node object

    def connect(self, node1, node2):                # connect 2 nodes in memory
        node1.children.add(node2)
        node2.children.add(node1)

    def turnToNode(self, mouse, node):              # provide physical direcives to mouse
        pass

    def turnToLocation(self, mouse, pos):           # provide physical direcives to mouse
        pass

    def turnToDirection(self, mouse, direction):    # turn to a particular direction
        pass

    def getPos(self, mouse, direction):
        pass

    def add(self, x,y):
        pass

    def get(self, x,y):
        try:
            return a[str((x,y))]
        except:
            a[str((x,y))] = Node(x,y)
            return a[str((x,y))]
        pass


# Mouse will store info regarding it's position and direction
class Mouse():

    def __init__(self):
        self.node = None 
        self.direction = None
        self.pos = None
        self.api = API

    def scan(self):                             # scan the neighbours and walls around it
        #check forward
        if not self.api.wallFront():
            n = manager.getPos(self, 'f') 
            manager.connect(self.node, manager.get(n.x,n.y))
        #check left
        if not self.api.wallLeft():
            n = manager.getPos(self, 'l') 
            manager.connect(self.node, manager.get(n.x,n.y))
        #check right
        if not self.api.wallRight():
            n = manager.getPos(self, 'r') 
            manager.connect(self.node, manager.get(n.x,n.y))

    def left(self):                             # wrapper of turnLeft()
        self.api.turnLeft()

    def right(self):                            # wrapper of turnRight()
        self.api.turnRight()

    def forward(self, distance = 1):            # wrapper of moveForward()
        self.api.moveForward(distance)

    def moveTo(self, node):
        turnToNode(self, node)
        self.forward()
        self.node = node
        self.pos = self.node.pos


def traverse(parent):
    for i in parent.children:
        mouse.moveTo(i)
    mouse.moveTo(parent)


def log(string):
    sys.stderr.write("{}\n".format(string))
    sys.stderr.flush()

def main():
    global mouse, manager
    head = Node(0,0)
    mouse = Mouse()
    manager = Manager()
    mouse.node = head
    mouse.scan()
    traverse(head)
    
if __name__ == "__main__":
    main()
