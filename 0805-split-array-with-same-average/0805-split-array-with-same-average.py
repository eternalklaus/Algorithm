class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        import math
        quotient, divisor = sum(nums), len(nums)
        gcd = math.gcd(quotient, divisor)
        quotient, divisor = quotient//gcd, divisor//gcd
        
        def fit(q,d):
            gcd = math.gcd(q, d)
            return q//gcd == quotient and d//gcd == divisor

        if len(nums)==1: return False
        
        currsum = defaultdict(set) # set = {(100, 2)} => 토탈합이 100이고 갯수는 2개 
        currsum[0] = {(0,0), (nums[0], 1)}
        # inline calc
        if fit(nums[0], 1): return True

        for i, n in enumerate(nums):
            if i == 0: continue 
            for befsum, beflen in currsum[i-1]:
                currsum[i].add((befsum, beflen)) # nums[i]를 더하지 않은경우
                if beflen >= len(nums)//2: continue ### !!! 
                currsum[i].add((befsum+nums[i], beflen+1)) # nums[i]를 더한 경우    

                # inline calc
                if fit(befsum+nums[i], beflen+1): return True

        # for suum, leen in currsum[len(nums)-1]:
        #     if leen == 0 or leen == len(nums): continue
        #     if fit(suum, leen): return True
        return False
        