class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        L = len(beans)
        
        sums = [0] * L
        
        for i in range(L):
            sums[i] = sums[i-1] + beans[i] 
        
        output = sums[-1] - beans[0] * L # bound of all numbers are beans[0] 
        for idx, bean in enumerate(beans):
            left = sums[idx] # 
            right = sums[-1] - sums[idx] - (beans[idx] * (L - idx)) # bound of all numbers are beans[idx]
            output = min(output, left+right)
        return output 