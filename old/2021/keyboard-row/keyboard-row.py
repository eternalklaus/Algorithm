class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        output = []
        from collections import Counter
        row1 = set('qwertyuiop')
        row2 = set('asdfghjkl')
        row3 = set('zxcvbnm')
        
        for word in words:
            w = word.lower()
            wc = set(w)
            if wc.issubset(row1) or wc.issubset(row2) or wc.issubset(row3):
                output.append(word)
        return output
            
            