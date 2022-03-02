class Solution:
    def canJump(self, nums: List[int]) -> bool:
        L = len(nums)
        checked = [False] * L
        checked[-1] = True
        
        for i in range(L-1, -1, -1):
            ti = i + nums[i] # target index
            if ti >= L-1:
                checked[i] = True
            if True in checked[i:ti+1]:
                checked[i] = True
        
        return checked[0]
            