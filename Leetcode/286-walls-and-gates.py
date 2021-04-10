class Solution(object):
    def __init__(self):
        self.queue = []
        self.rooms = None 
        self.COL = -1
        self.ROW = -1

    def init(self, rooms): 
        self.rooms = rooms 
        self.COL = len(rooms)
        self.ROW = len(rooms[0])
        for c in xrange(self.COL): # init queues
            for r in xrange(self.ROW):
                if rooms[c][r] == 0: # gate
                    self.queue.append([c, r])
        
    def wallsAndGates(self, rooms):
        self.init(rooms)

        while len(self.queue) > 0:
            [c,r] = self.queue.pop(0)
            disatance = self.rooms[c][r] + 1

            if c-1 >= 0:
                if self.rooms[c-1][r] == 2147483647:
                    self.rooms[c-1][r] = disatance
                    self.queue.append([c-1, r])
            
            if r-1 >= 0:
                if self.rooms[c][r-1] == 2147483647:
                    self.rooms[c][r-1] = disatance
                    self.queue.append([c, r-1])

            if c+1 < self.COL:
                if self.rooms[c+1][r] == 2147483647:
                    self.rooms[c+1][r] = disatance
                    self.queue.append([c+1, r])

            if r+1 < self.ROW:
                if self.rooms[c][r+1] == 2147483647:
                    self.rooms[c][r+1] = disatance
                    self.queue.append([c, r+1])

