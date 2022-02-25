class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # coins.sort(reverse=True)
        L = len(coins)
        
        @cache
        def getcoinnum(idx, amount):
            if amount == 0:
                return 0
            if idx >= L:
                return float('inf')
            if amount < coins[idx]:
                return getcoinnum(idx+1, amount) # pass this coin.
            
            else:
                # include this coin 
                num1 = 1 + getcoinnum(idx, amount - coins[idx])
                # declude this coin
                num2 = getcoinnum(idx+1, amount)
                return min(num1, num2)
        
        output = getcoinnum(0, amount)
        if output >= float('inf'):
            return -1
        return output