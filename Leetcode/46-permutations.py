class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms, total = [], len(nums)
        def appendsubset(used):
            nonlocal perms
            if len(used) == total:
                perms.append(used)
                return 
            else: 
                left = [x for x in nums if x not in used]
                for c in left:
                    tused = used.copy()
                    tused.append(c)
                    appendsubset(tused)

        appendsubset([])
        return perms