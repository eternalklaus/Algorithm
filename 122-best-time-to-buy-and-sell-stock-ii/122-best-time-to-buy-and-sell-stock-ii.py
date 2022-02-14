class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two state: hold -> sold / sold -> hold 
        hold, sold = -prices[0], 0
        
        for price in prices[1:]:
            hold_bk = hold 
            hold = max(hold, sold - price)
            sold = max(sold, hold_bk + price)
        return sold
            