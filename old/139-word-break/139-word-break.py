class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 재귀함수 리턴이 bool이도록 만들기
        # time complexity 계산하기 
        L, wordDict = len(s), set(wordDict)
        
        @cache
        def breakable(idx):
            if idx == L:
                return True 
            for i in range(idx+1, L+1): ###
                word = s[idx:i]
                if word in wordDict and breakable(i):
                    return True
            return False 
        
        return breakable(0)
            