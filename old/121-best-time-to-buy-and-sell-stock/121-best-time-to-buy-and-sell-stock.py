class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, profit = float('inf'), -float('inf')
        for price in prices:
            sell = price 
            
            profit = max(profit, sell-buy)
            buy = min(buy, price)
            
        return max(profit, buy-price)