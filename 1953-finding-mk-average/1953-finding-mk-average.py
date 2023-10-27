class MKAverage:
    
    def __init__(self, m: int, k: int):
        from sortedcontainers import SortedList
        self.m = m
        self.k = k
        self.sum = 0
        self.numssort = SortedList() # add-O(logn) pop-O(logn) bisect_left-O(logn) index-O(logn) remove-O(logn)
        self.numstime = Deque() # popleft-O(1)
        self.initialized = False

    def addElement(self, num: int) -> None:
        self.numstime.append(num)
        self.numssort.add(num)

        if len(self.numstime) < self.m:
            self.sum += num

        elif len(self.numstime) == self.m:
            self.sum += num
            # initialize the sort...
            for i in range(self.k):
                li = i
                ri = -i - 1
                self.sum = self.sum - self.numssort[li] - self.numssort[ri]

        elif len(self.numstime) == self.m + 1:
            # include the result of inserting num into numssort
            n = num
            i = self.numssort.index(n)
            if i < self.k: # left
                self.sum += self.numssort[self.k]
            elif i >= len(self.numssort) - self.k: # right
                self.sum += self.numssort[-self.k-1]
            else: # middle
                self.sum += n

            # delete the stale number
            n = self.numstime.popleft()
            i = self.numssort.bisect_left(n)
            if i < self.k: # left
                self.sum -= self.numssort[self.k] 
            elif i >= len(self.numssort) - self.k: # right
                self.sum -= self.numssort[-self.k-1]
            else: # middle
                self.sum -= n
            self.numssort.remove(n)

    def calculateMKAverage(self) -> int:
        if len(self.numssort) == self.m:
            return self.sum // (self.m - 2 * self.k)
        return -1
        

# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()