
# TIME LIMIT EXCEED.....
class Solution(object):
    def maxArea(self, height):

        sortedidx = sorted(range(len(height)), key=lambda i:height[i], reverse=True) 
        #print sortedidx
        length = len(height)
        maxarea = 0
        breakit = False
        for j in range(0, len(sortedidx)):
            if breakit is True: break

            for i in range(0, j):
                if breakit is True: break

                #optimization
                if height[sortedidx[j]] * length < maxarea: 
                    breakit = True 

                area = abs((sortedidx[i]-sortedidx[j]) * height[sortedidx[j]])
                # print 'i=%d j=%d area=%d'%(sortedidx[i], sortedidx[j], area)
                if area > maxarea:
                    maxarea = area

        return maxarea

sl = Solution()
print sl.maxArea( [1,0,0,0,0,0,0,2,2])