class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        #       [1 5 3 2]
        # deque [1 2 3 0]
        
        def clean_right(n): # 4
            while deque:
                i = deque[-1]
                if nums[i] <= n:
                    deque.pop()
                else: 
                    break
        
        def clean_left(i):
            while deque:
                i2 = deque[0]
                if i - i2 >= k: 
                    deque.popleft()
                else:
                    break
        
        deque = deque() # popleft()
        output = []
        # for i, n enumerate(nums):
        for i in range(len(nums)):
            # print (deque)
            n = nums[i]
            clean_right(n)
            deque.append(i)
            clean_left(i)
            
            if i >= k-1:
                output.append(nums[deque[0]])
        
        return output