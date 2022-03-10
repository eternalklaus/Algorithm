class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        output = []
        for num in nums: # num = 4
            idx = -1 # 
            for i, val in enumerate(output): # output = [1,2,3,6,8]
                if val >= num: # 신흥강자 ### 같은것도 카운팅해서 idx로 쳐줘야 아래else문으로 안감
                    idx = i
                    break
            if idx >= 0:
                output[idx] = num 
            
            else: # output = [1,2,3]
                output.append(num)
                
        return len(output)
            