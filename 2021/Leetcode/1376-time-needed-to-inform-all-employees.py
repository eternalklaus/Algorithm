class Solution:
    def getmaxttl(self):
        maxval = -1
        for i in range(len(self.ttl)):
            if self.ttl[i] > maxval:
                maxval = self.ttl[i]
        return maxval

    def updatettl(self, idx):
        ie  = idx               # index_employy
        im  = self.manager[idx] # index_directmanager 
        
        if im == -1: # this ie is the boss 
            self.ttl[ie] = 0

        elif self.ttl[im] == -1:
            self.updatettl(im)
            self.ttl[ie] = self.ttl[im] + self.informTime[im]
        
        else:
            self.ttl[ie] = self.ttl[im] + self.informTime[im]

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        self.manager    = manager 
        self.informTime = informTime
        self.ttl        = [-1] * len(informTime) # time to listen
        
        for i in range(len(self.ttl)):
            self.updatettl(i)
        
        retval = self.getmaxttl()
        return retval
        