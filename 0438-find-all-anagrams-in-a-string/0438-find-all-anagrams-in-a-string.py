class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pcounter = Counter()
        scounter = Counter()
        output = []

        for c in p:
            pcounter[c] += 1
        left = 0
        right = -1
        
        while True:
            right += 1
            if right >= len(s): break
            
            scounter[s[right]] += 1
            while right - left + 1 > len(p):
                scounter[s[left]] -= 1
                left += 1
            if right - left + 1 == len(p):
                if pcounter == scounter: output.append(left)
        
        return output