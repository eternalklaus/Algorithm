class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordset = set(words) ###1
        @cache ###2
        def dfs(word):
            for i in range(1, len(word)): ### 최초에 전달되는 word부터 쪼개야 함. 바로 word in wordset 때리면 안됨~
                if word[:i] in wordset and word[i:] in wordset:
                    return True 
                if word[:i] in wordset and dfs(word[i:]):
                    return True 
                ### if dfs(word[:i]) and word[i:] in wordset: ###3
            return False 
    
        output = []
        for word in words:
            if dfs(word):
                output.append(word)
        return output 
                    