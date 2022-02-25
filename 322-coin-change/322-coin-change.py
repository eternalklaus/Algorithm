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
                num1 = 1 + getcoinnum(idx, amount - coins[idx]) # include this coin 
                num2 = getcoinnum(idx+1, amount) # declude this coin
                return min(num1, num2)
        
        output = getcoinnum(0, amount)
        return output if output < float('inf') else -1