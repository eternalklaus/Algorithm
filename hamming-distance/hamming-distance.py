class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # count different bit
        z = x ^ y
        z_bin = bin(z)[2:] # remove leftmost '0x'
        return z_bin.count('1')
        