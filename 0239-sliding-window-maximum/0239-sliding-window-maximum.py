class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        
        def cleanright(n):
            while idxdeque:
                i = idxdeque[-1]
                if nums[i] <= n:
                    idxdeque.pop()
                else:
                    break
        
        def cleanleft(i):
            while idxdeque:
                if i - idxdeque[0] >= k:
                    idxdeque.popleft()
                else: 
                    break
        
        idxdeque = deque()
        output = []
        for i, n in enumerate(nums):
            cleanright(n) # n보다 약한것들 정리
            idxdeque.append(i)
            cleanleft(i) # 이미 죽은것들 정리
            # print (idxdeque)
            if i >= k-1:
                output.append(nums[idxdeque[0]])
        return output
                
            