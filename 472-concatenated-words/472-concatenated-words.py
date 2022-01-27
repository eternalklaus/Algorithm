class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordset = set(words)
        
        @cache
        def dfs(word):
            for i in range(1,len(word)):
                prefix, suffix = word[:i], word[i:]
                # print (prefix, suffix)
                if prefix in wordset and suffix in wordset:
                    return True 
                if prefix in wordset and dfs(suffix):
                    return True 
            return False 
        
        output = []
        for word in wordset:
            if dfs(word): 
                output.append(word)
        return output 
        
                