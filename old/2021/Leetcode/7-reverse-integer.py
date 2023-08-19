class Solution:
    def reverse(self, x: int) -> int:
        sign = [-1, 1][x > 0]
        qut, ret = x*sign, 0
        while qut != 0 and qut != -1:
            rem = qut%10
            qut = qut//10
            ret = ret*10 + rem 
        ret = ret*sign
        return ret if -2**31 <= ret <= 2**31 - 1 else 0
