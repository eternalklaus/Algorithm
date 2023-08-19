class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        I, J, L = rows, cols, len(sentence)
        # starting j = 0
        # si = wordindex 
        # how many words are fitting on specific line?
        
        @cache 
        def lineword(wordidx):
            j, wordcnt = -1, 0
            
            while True:
                j += (1 + len(sentence[wordidx])) # add "-"
                if j > J: break # OK until j reaches J
                
                wordcnt += 1 
                wordidx = (wordidx + 1) % L
            return wordcnt 
        
        output, wordidx = 0, 0
        for i in range(I):
            wordcnt = lineword(wordidx)
            output += wordcnt
            wordidx = (wordidx + wordcnt) % L
        return output // L 