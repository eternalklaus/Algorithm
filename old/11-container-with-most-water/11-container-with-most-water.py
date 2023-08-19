class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        output = 0
        
        while left < right:
            output = max(output, (right-left) * min(height[left], height[right]))
            
            # left -->
            if height[left] <= height[right]:
                left += 1
            
            # <-- right
            else:
                right -= 1
        
        return output 