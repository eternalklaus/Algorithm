class Solution:
    def alienOrder(self, words: List[str]) -> str:
        L = len(words)
        
        firstnext = defaultdict(list)
        nextfirst = defaultdict(list)
        charset = set()
        
        def del_common_prefix(word1, word2):
            L = min(len(word1), len(word2))
            for i in range(L):
                if word1[i] != word2[i]:
                    return word1[i], word2[i]
            x = '' if len(word1) == L else word1[L]
            y = '' if len(word2) == L else word2[L]
            return x, y
        
        def updatecharset(word):
            charset.update(set(word)) ###
            
        # step1. draw graph
        updatecharset(words[0])
        for i in range(1, L):
            updatecharset(words[i])
            x, y = del_common_prefix(words[i-1], words[i])
            if x and not y: return '' # invalid order 
            if not x: continue
            firstnext[x].append(y)
            nextfirst[y].append(x)
            
        # step2. find leaf (next that has no first)
        queue = []

        for ch in charset:
            # if y not in nextfirst:
            # print (ch, nextfirst.get(ch), not nextfirst.get(ch))
            if not nextfirst.get(ch):
                queue.append(ch)
        # print (queue)
        # drop leaf by leaf, gather leaves
        output = ''
        while queue:
            leaf = queue.pop(0)
            output += leaf
            
            for nextleaf in firstnext[leaf]:
                nextfirst[nextleaf].remove(leaf) # leaf is already dropped, so we'll not take account of it.
                if not nextfirst[nextleaf]:
                    queue.append(nextleaf) 
        
        # print (output)
        if len(charset) == len(output): # leaves not handled is left
            return output
        return ''