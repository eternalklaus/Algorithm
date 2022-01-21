class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalsum = sum(nums)
        if totalsum % 2 == 1: return False
        targetsum = sum(nums)//2
        # print ('totalsum: %d, targetsum: %d'% (totalsum, targetsum))
        counter = Counter(nums)
        numbers = list(counter.keys())
        
        @cache
        def getsum(currentsum, i):
            # print (currentsum, i)
            # base case 
            if currentsum == targetsum:
                return True 
            if currentsum > targetsum:
                return False 
            if i >= len(numbers):
                return False 
            
            # iterate and take count num one by one 
            num = numbers[i]
            
            # exclude the num(skip)
            output = getsum(currentsum, i+1)
            if output: return True 
            
            # include the num
            for c in range(counter[num]):
                currentsum += num 
                output = getsum(currentsum, i+1)
                if output: return True 
            return False 
        
        return getsum(0, 0)
                
                    