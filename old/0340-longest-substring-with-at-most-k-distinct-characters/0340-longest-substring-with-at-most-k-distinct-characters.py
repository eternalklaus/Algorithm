class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # occur = 카운터에 저장 cnt = {c:3 d:1}
        # 슬라이딩 윈도우로 한칸씩 이동
        # 슬라이딩 윈도우의 이동전략:
        #   ㄴ right: 한칸씩 이동
        #   ㄴ left: len(occur) > k라면, len(occur) < k일때까지 이동
        occur = Counter()
        left, right = 0, -1
        output = 0
        while True: 
            right += 1
            if right >= len(s): break

            occur[s[right]] += 1

            while len(occur) > k:
                occur[s[left]] -= 1
                if occur[s[left]] == 0:
                    del occur[s[left]]
                left += 1

            output = max(right - left + 1, output)
        
        return output