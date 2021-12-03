class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def getprod(mylist):
            if len(mylist) == 0: return 0
            output = 1
            for n in mylist:
                output *= n
            return output
        
        def getmaxprod(mynums):
            if len(mynums) == 0: return 0
            elif len(mynums) == 1: return mynums[0]
            
            # get all of the indexs of minus value
            minusidxs = []
            for i, n in enumerate(mynums):
                if n < 0: minusidxs.append(i)
            
            
            if len(minusidxs) % 2 == 0: # prod would be plus
                return getprod(mynums)
            
            else: # we need to remove one minus value (left or right)
                mini, maxi = minusidxs[0], minusidxs[-1]
                return max(getprod(mynums[mini+1:]), getprod(mynums[:maxi]))
        
        
        lists = []
        if 0 not in nums:
            return getmaxprod(nums)
        
        # split by 0
        temp = [] 
        for n in nums:
            if n == 0: # if 0 is appeared
                if not lists: lists.append([0]) # append 0 either ONLY in the first time
                lists.append(temp)
                temp = [] # flush temp
            else:
                temp.append(n)
        lists.append(temp) # append the last list
        
        output = nums[0]
        for l in lists:
            output = max(output, getmaxprod(l))
        return output