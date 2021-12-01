class Solution:
    def rob(self, nums: List[int]) -> int:
        # Recursion with memoization
        # Time: O(n) Space O(n) by recursion stack
        '''
        @cache
        def getmax(start):
            if start >= len(nums): 
                return 0
            
            return max(nums[start] + getmax(start+2), getmax(start+1))
        return getmax(0)
        '''
        
        # Dynamic programming : Tabular approach 
        # Time: O(n) / Space: O(n)
        '''
        saved = [0 for _ in range(len(nums))]
        
        N = len(nums) 
        saved[N-1] = nums[N-1]
        saved[N-2] = max(nums[N-2], nums[N-1])
        
        for i in range(N-3, -1, -1): 
            saved[i] = max(saved[i+1], nums[i] + saved[i+2]) 
        
        return max(saved)
        '''
        
        # Dynamic programming : Tabular approach 
        # 
        N = len(nums)
        rob_next = max(nums[N-1], nums[N-2]) 
        rob_next_plus_one = nums[N-1]
        current = max(rob_next, rob_next_plus_one)
        for i in range(N-3, -1, -1):
            current = max(rob_next, rob_next_plus_one + nums[i])
            # print ('i=%d current=%d rob_next=%d, rob_next_plus_one=%d' % (i, current,rob_next,rob_next_plus_one))
            rob_next_plus_one = rob_next
            rob_next = current
        return current