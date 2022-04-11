class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        from collections import defaultdict
        idxdict, output = defaultdict(list), 0
        
        for word in words:
            idxdict[word[0]].append(word[1:]) # word[1:] can be ''
            
        for i, c in enumerate(s):
            idxwords = idxdict.pop(c, []) ###
            for word in idxwords:
                if word == '': 
                    output += 1
                else:
                    idxdict[word[0]].append(word[1:])
                
        return output 
                
            