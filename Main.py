import API
import sys
import time

class Node():

    def __init__(self, node, alphabet):
        self.u = None
        self.d = None
        self.l = None
        self.r = None

        if alphabet=='U':
            self.x = node.x
            self.y = node.y+1
        if alphabet=='R':
            self.x = node.x+1
            self.y = node.y
        if alphabet=='D':
            self.x = node.x
            self.y = node.y-1
        if alphabet=='L':
            self.x = node.x-1
            self.y = node.y

        self.var = -1

    def get_neighbours_list(self):
        ls = []
        if self.l :
            ls.append(self.l)
        if self.r :
            ls.append(self.r)
        if self.u :
            ls.append(self.u)
        if self.d :
            ls.append(self.d)
        return ls 

    def get_neighbours_dict(self):
        return {"u":self.u,"r":self.r,"d":self.d,"l":self.l}

    def n_neighbours(self):
        c = 0
        if self.l :
            c += 1
        if self.r :
            c += 1
        if self.u :
            c += 1
        if self.d :
            c += 1
        return c 


def log(string):
    sys.stderr.write("{}\n".format(string))
    sys.stderr.flush()

def main():
  
if __name__ == "__main__":
    main()
