class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 금액별 최소코인수 업데이트 
        
        coinnum = [float('inf')] * (amount+1)
        coinnum[0] = 0
        
        for price in range(1, amount+1):
            for coin in coins: # can use all kind of coins every session 
                if price - coin < 0: continue
                coinnum[price] = min(coinnum[price], coinnum[price-coin]+1)
        
        return coinnum[-1] if coinnum[-1] < float('inf') else -1
                
                