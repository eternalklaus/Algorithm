class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = lambda x:len(x))
        wordlen, output = {}, 0
        
        for word in words:
            bwl = 0 
            for i, c in enumerate(word):
                bw = word[:i] + word[i+1:] # before word
                bwl = max(bwl, wordlen.get(bw) or 0) # before word len 
            wordlen[word] = bwl + 1 
            output = max(output, wordlen[word])
        return output 
            
                