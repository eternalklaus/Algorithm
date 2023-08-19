class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold, hold, justsold = 0, -prices[0], -prices[0]
        
        for price in prices[1:]:
            hold = max(hold, sold-price)
            sold = max(justsold, sold) # 이전스텝의 justsold 이거나 sold
            justsold = hold + price # 현재스텝의 justsold 업데이트
        
        return max(sold, justsold)
            
            