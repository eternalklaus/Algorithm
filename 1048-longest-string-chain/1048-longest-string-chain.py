class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = lambda x:len(x))
        
        chainlen = {} 
        output = 0
        for word in words:
            maxlen = 0
            for i, _ in enumerate(word): # 'abc' -> ab:5, bc:2, ac:1 
                pdc = word[:i] + word[i+1:] 
                pdcl = chainlen.get(pdc) or 0 
                maxlen = max(maxlen, pdcl+1)
            chainlen[word] = maxlen
            output = max(output, chainlen[word])
        return output 