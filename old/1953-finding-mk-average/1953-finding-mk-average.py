class MKAverage:
    def __init__(self, m: int, k: int):
        from sortedcontainers import SortedList
        self.m = m
        self.k = k
        self.slist = SortedList() # sorted list
        self.tlist = Deque() # timed list 
        self.sum = 0
        
    def addElement(self, num: int) -> None:
        m, k = self.m, self.k

        if len(self.tlist) < m-1:
            self.tlist.append(num)
            self.slist.add(num)
            self.sum += num

        # initialize sum (최초 1회)
        elif len(self.tlist) == m-1: 
            self.tlist.append(num)
            self.slist.add(num)
            self.sum += num
            for i in range(k):
                self.sum -= self.slist[i]
                self.sum -= self.slist[-i-1]

        # remove oldest one
        elif len(self.tlist) == m:
            self.tlist.append(num)
            self.slist.add(num)
            
            # take account of the added one (이미 박혀있음)
            i = self.slist.index(num)
            if i < k: 
                self.sum += self.slist[k]
            elif i >= len(self.slist) - k: ###
                self.sum += self.slist[-k-1]
            else:
                self.sum += num
            
            # take account of the subtracted one (이미 박혀있음)
            n = self.tlist.popleft()
            i = self.slist.bisect_left(n)
            if i < k:
                self.sum -= self.slist[k]
            elif i >= len(self.slist) - k:
                self.sum -= self.slist[-k-1]
            else:
                self.sum -= n
            self.slist.remove(n)
            
    def calculateMKAverage(self) -> int:
        if len(self.slist) < self.m:
            return -1
        return self.sum // (self.m - self.k - self.k)
        


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()