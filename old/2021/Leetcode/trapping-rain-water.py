class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water = height[:]
        sortedidx = sorted(range(len(height)), key=lambda x:height[x], reverse=True)

        for i in range(1, len(water)):
            idx = sortedidx[i]
            if water[idx] !=  height[idx]: continue # already water fulled. so skip it.
            
            # compare distance until sortedidx[0~me] and full water into shortest one.
            lclosei = idx 
            rclosei = idx
            rlength = len(water)
            llength = len(water)
            
            for j in range(0, i):
                
                idx2 = sortedidx[j]
                # print 'idx %d, %d' % (idx, idx2)
                # --- nearist on right side --- 
                if idx < idx2:
                    if idx2 - idx < rlength:
                        rclosei = idx2
                        rlength = idx2 - idx
                        continue
                
                # --- nearist on left side --- 
                if idx2 < idx:
                    if idx - idx2 < llength:
                        lclosei = idx2
                        llength = idx - idx2
                        continue 
                
            # fill the water from lclosei ~ i and i ~ rclosei
            for j in range(lclosei + 1, idx): # <- watch out -1
                water[j] = height[idx]
            
            for j in range(idx, rclosei):
                water[j] = height[idx]

         
        # print height
        # print water
        sum = 0 
        for i in range(len(height)):
            sum += water[i] - height[i]
        
        return sum


sl = Solution()
print sl.trap([0,1,0,2,1,0,1,3,2,1,2,1])