class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        intervals.sort()
        prevl, prevr = -1, -1
        
        for l, r in intervals:
            '''
            .              l.    r
             prevl prevr
            '''
            if prevr < l:
                output.append([prevl, prevr])
                prevl = l
                prevr = r
                continue 
            
            '''
                   l.        r
             prevl.  prevr
            '''
            # if overlapped, just update those numbers...
            prevl = min(l, prevl)
            prevr = max(r, prevr)
        
        # new one created, but not appended becouse of for loop ends
        if output[-1] != [prevl, prevr]: 
            output.append([prevl, prevr])
        output.pop(0) # remove [-1, -1]
        return output 
            