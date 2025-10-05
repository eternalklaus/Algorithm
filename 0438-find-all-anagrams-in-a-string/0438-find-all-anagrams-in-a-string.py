class Solution:
    from itertools import permutations
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 가능한 p의 모든 케이스들을 set에 저장 
        # s를 돌면서 모든 윈도우에 대해 if window in set: output.append(i) 수행

        l = []
        output = []

        for c in p: l.append(c)
        perm = set()
        for perm_str in permutations(l):
            perm.add(''.join(perm_str))

        left = 0
        right = -1
        while True: 
            right += 1
            if right >= len(s): break 
            if right - left + 1 > len(p):
                left += 1
            if right - left + 1 == len(p):
                curr_str = ''.join(s[left:right+1])
                if curr_str in perm: 
                    output.append(left)
        
        return output

        