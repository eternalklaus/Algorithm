class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        # sub one element, add two element/2.
        # make target
        from math import log2
        
        if sum(nums) < target: return -1
        
        # looking at the lowest bit -> and go up
        cnt = Counter()
        for num in nums:
            cnt[int(log2(num))] += 1
        
        output = 0
        for i in range(31):
            if target & 2**i: 
                print (i, cnt)
                if cnt[i] > 0: 
                    cnt[i] -= 1
                else: # 쪼개야할 때
                    cnt[i] += 2 # 마지막놈은 2개가 되지만
                    cnt[i] -= 1 # 하나를 사용할 것이므로 
                    j = i + 1
                    while True:
                        if cnt[j] > 0:
                            cnt[j] -= 1 # 하나를 소모
                            break
                        cnt[j] += 1 # trail을 남긴다...
                        j += 1

                    output += (j - i)

            cnt[i+1] += (cnt[i] // 2) # 처리하고 남은것들을 올려보낸다 
        return output 

                    
