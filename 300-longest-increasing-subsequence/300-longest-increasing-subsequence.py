class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        output = []
        for num in nums:
            for i, _ in enumerate(output):
                if output[i] >= num: ### =필수!
                    output[i] = num
                    break
            else: 
                output.append(num)
        
        
        return len(output)