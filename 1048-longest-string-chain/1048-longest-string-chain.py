class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # order words by its length!!
        words.sort(key=lambda x:len(x))
        # print (words)
        
        chainlen, output = {}, 0 
        for word in words:
            wordval = 0
            for i, c in enumerate(word):
                befword = word[:i] + word[i+1:]
                befwordval = chainlen.get(befword) or 0
                
                wordval = max(wordval, befwordval + 1)
                
            chainlen[word] = wordval
            output = max(output, wordval)
        
        # print (chainlen)
        return output 
        