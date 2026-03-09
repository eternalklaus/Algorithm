class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        L = len(nums)
        nums = [nums[i] % modulo == k for i in range(L)]
        accum = [0] * L

        for i in range(L):
            if i == 0:
                accum[0] = nums[0]
            else:
                accum[i] = accum[i-1] + nums[i]
        
        print (accum)
        counter = Counter() # 몫이 0, 1, 2, ... , modulo-1 인 것들의 모임 
        # 만약 k=2이고, 현재 accum이 3(나머지1)이라면? 1(나머지2)인것의 개수를 세는거지. 
        # 만약 k=2이고, 현재 accum이 1(나머지1)이라면? modulo-1(나머지2) 인것의 개수를 세는거지 
        output = 0
        counter[0] = 1
        for i in range(L):
            # 만약 나 혼자서도 완전하다면? 내가 k그자체라면?
            key = (accum[i] - k) % modulo
            
            # print ("accum = %d key = %d" % (accum[i], key))
            # print (counter)
            # print ('')
            output += counter[key]

            counter[accum[i] % modulo] += 1
            
        return output

            