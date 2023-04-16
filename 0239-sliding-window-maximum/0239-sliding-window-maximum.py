class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # O(n) 
        def clean_right(n):
            while numbers:
                i = numbers[-1]
                if nums[i] <= n:
                    numbers.pop()
                else:
                    break
        
        def clean_left(i):
            while numbers:
                i2 = numbers[0]
                if i - i2 >= k: 
                    numbers.pop(0)
                else:
                    break
            
        output = []
        numbers = []
        for i in range(len(nums)):
            n = nums[i]
            clean_right(n)
            numbers.append(i)
            clean_left(i)
            
            if i >= k-1:
                output.append(nums[numbers[0]])
        
        return output 