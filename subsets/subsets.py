class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def getsubsets(left, subset):
            nonlocal result
            result.append(subset)
            for i, n in enumerate(left):
                # be careful..!!! subset.append(n) isnt return subset
                subset_copy = subset.copy()
                subset_copy.append(n)
                getsubsets(left[i+1:], subset_copy) # .. we should copy subset before passing parameter..
                
        getsubsets(nums, [])
        return result