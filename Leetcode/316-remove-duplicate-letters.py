class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        from collections import Counter 
        cnt, left, right = Counter(s), '1', s

        while right:
            c, right = right[0], right[1:]

            # c is already exist in left
            if c in left:
                continue # don't append c 
            
            # 1) c is smaller then before
            while left[-1] in right and left[-1] >= c:
                left = left[:-1]
            left += c

        return left[1:]