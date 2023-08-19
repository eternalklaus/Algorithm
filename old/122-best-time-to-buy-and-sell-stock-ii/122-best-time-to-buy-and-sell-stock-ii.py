class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # state: bought, sold 
        hold, sold = -prices[0], 0
        for price in prices[1:]:
            sold = max(sold, hold+price)
            hold = max(hold, sold-price)

        return sold
            
            