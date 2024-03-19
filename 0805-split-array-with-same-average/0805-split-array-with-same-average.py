class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        import math
        quotient, divisor = sum(nums), len(nums)
        gcd = math.gcd(quotient, divisor)
        quotient, divisor = quotient//gcd, divisor//gcd
        L = len(nums)

        def fit(q,d):
            gcd = math.gcd(q, d)
            return q//gcd == quotient and d//gcd == divisor
        
        sums = defaultdict(set) # sums[원소갯수] = 원소들의합
        sums[0] = {0}
        for i in range(L):
            # nums[i]까지 왔다? 그럼 조합의 최대길이는 i+1
            # for j in range(i,-1,-1): # sums[3]의 모든것들에 num을더해 sums[4]로 보낸다. 2를3으로 보낸다. 1을 2로보낸다.
            for j in range(min(i, L//2), -1, -1):
                for befsum in sums[j]:
                    sums[j+1].add(befsum+nums[i])
                    if j+1 != L and fit(befsum+nums[i], j+1): return True
        return False
        
        
                