class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # O(1) space
        '''
        nums.sort()
        return nums[len(nums)//2]
        '''
        
        # O(1) space - Boyer-Moor Algorithm
        output = None
        counter = 0
        for n in nums:
            if counter == 0: # change candidate
                output = n
                counter = 1
            else: # upvote/downvote counter
                if output == n:
                    counter += 1
                else:
                    counter -= 1
        return output
                
            
            