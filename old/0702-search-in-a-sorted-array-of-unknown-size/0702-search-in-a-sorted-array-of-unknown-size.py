# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        li = 0
        ri = 10 ** 4
        while li <= ri:
            mi = (li + ri) // 2
            val = reader.get(index=mi) 
            if val == target:
                return mi
            elif val < target:
                li = mi + 1
            else:
                ri = mi - 1

        return -1