class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        # if overlapped range appears, ignore the overlapped area. 
        wall = [i for i in range(100000)]
        output = []
        for i, [start, end] in enumerate(paint):
            start = start - 1
            end = end - 1
            
            li = bisect.bisect(wall, start)
            ri = bisect.bisect(wall, end)
            area = ri - li
            output.append(area) # append the range 
            
            while area:  # if the area == 3 -> 3, 2, 1
                wall.pop(li)
                area -= 1
        
        return output 