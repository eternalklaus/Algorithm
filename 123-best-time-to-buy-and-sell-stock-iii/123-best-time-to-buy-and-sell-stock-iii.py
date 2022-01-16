class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = len(prices)
        l2r = [0 for _ in range(L)]
        r2l = [0 for _ in range(L)]
        
        l2r[0], r2l[L-1] = 0, 0

        # left to right max diff (down->up)
        minval = prices[0]
        for i in range(1, L):
            l2r[i] = max(l2r[i-1], prices[i] - minval)
            minval = min(prices[i], minval)
            
        # right to left max diff (down<-up)
        maxval = prices[L-1]
        for i in range(L-2, -1, -1):
            r2l[i] = max(r2l[i+1], maxval - prices[i])
            maxval = max(prices[i], maxval)
        
        output = 0 
        # consider the case having TWO transaction
        for i in range(0, L-1):
            output = max(output, l2r[i] + r2l[i+1]) # l2r[0], r2l[1] ~ l2r[L-2], l2r[L-1] 
        
        # consider the case having ONLY ONE transaction
        output = max(output, r2l[0]) 
        output = max(output, l2r[L-1])

        return output 