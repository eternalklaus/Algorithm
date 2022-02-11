class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, output = float('inf'), 0
        for price in prices:
            output = max(output, price-buy)
            buy = min(buy, price)
            # print (f'output:{output}, buy:{buy}')
        return max(output, buy-price)