class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = len(prices)
        
        # state = sell, hold, empty
        hold, justsold, sold = -prices[0], 0, 0
        for i in range(1, L):
            hold = max(hold, sold - prices[i])  # hold / buy new one now
            sold = max(justsold, sold)          # justsold can be taken account into form next step..
            justsold = hold + prices[i]
        
        return max(justsold, sold)