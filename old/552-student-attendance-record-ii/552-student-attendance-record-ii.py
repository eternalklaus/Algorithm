class Solution:
    def checkRecord(self, n: int) -> int:
        output = 0
        # clean -> late, clean, aclean
        # late -> twolate, clean, aclean
        # twolate -> clean, aclean
        
        # aclean -> alate, aclean
        # alate -> atwolate, aclean
        # atwolate -> aclean
        M = 10**9+7
        clean, late, twolate    = 1, 1, 0 # P, L, no
        aclean, alate, atwolate = 1, 0, 0 # A, no, no
        for i in range(n-1):
            aclean, alate, atwolate = (clean+late+twolate+aclean+alate+atwolate)%M, aclean, alate
            clean, late, twolate    = (clean+late+twolate)%M, clean, late
        
        return (aclean+alate+atwolate+clean+late+twolate) % M
            
            