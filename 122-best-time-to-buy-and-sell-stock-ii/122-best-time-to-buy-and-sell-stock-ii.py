class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # infinite number of buy-sell is possible 
        L = len(prices)
        output= 0
        buy, sell = prices[0], -float('inf')
        
        for i in range(0, L-1): # if downtrend starts, sell it before downtrend. 
            buy = min(buy, prices[i])
            
            if prices[i] > prices[i+1]: # downtrend starts. sell it beforehand(previous price)
                output += (prices[i] - buy)
                buy = prices[i+1]
            
            else: # uptrend. wait..
                'nothing to do..'
        
        output = max(output, output + (prices[-1]-buy))
        return output 
                
            