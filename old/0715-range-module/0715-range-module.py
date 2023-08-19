class RangeModule:

    def __init__(self):
        self.ranges = []
        
    def addRange(self, left: int, right: int) -> None:
        def merge():
            output = []
            prevl, prevr = -1, -1
            # prevl.  prevr
            #.              l      r
            for [l, r] in self.ranges:
                if l == r: continue # dealing with XXX
                if prevr < l:
                    output.append([prevl, prevr])
                    prevl = l
                    prevr = r
                else:
                    prevl = min(prevl, l)
                    prevr = max(prevr, r)
            if output and output[-1] == [prevl, prevr]: # already appended it 
                'do nothing'
            else:
                output.append([prevl, prevr])
            self.ranges = output
        # print (self.ranges)
        bisect.insort(self.ranges, [left, right])
        # print (self.ranges)
        merge()
        self.ranges.pop(0)
        # print (self.ranges)
        # print ('')
        
    def queryRange(self, left: int, right: int) -> bool:
        i = bisect.bisect(self.ranges, [left, right])
        # check if right one contains [left, right]
        if 0 <= i < len(self.ranges):
            rleft, rright = self.ranges[i]
            if rleft <= left and right <= rright:
                return True 
        # check if left one contains [left, right]
        if 0 <= i-1 < len(self.ranges):
            lleft, lright = self.ranges[i-1]
            if lleft <= left and right <= lright:
                return True
        return False

    def removeRange(self, left: int, right: int) -> None:
        ri = bisect.bisect(self.ranges, [left, right])
        i = ri
        # right overlapped
        while i < len(self.ranges):
            l, r = self.ranges[i]
            # left.     right
            #.      l.         r   (case1)
            #      l r             (case2)
            if l < right:
                if right < r: # case1
                    l = right
                    r = r
                    self.ranges[i] = [l, r]
                
                else:
                    self.ranges[i] = [l, l] # XXX: it should be deleted... 
            else: 
                break
            i += 1
        
        # left overlapped
        i = ri - 1
        if 0 <= i:
            l, r = self.ranges[i]
            # l               r
            #.   left.           right (case1)
            #.   left    right         (case2)
            if left < r:
                if r < right:
                    l = l
                    r = left
                    self.ranges[i] = [l, r]
                else:
                    del self.ranges[i]
                    self.ranges.insert(i, [right, r])
                    self.ranges.insert(i, [l, left])
        
# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)