class Trie:
    def __init__(self): # 이게 언발란스한 트리보다 큐연산할때 유리함
        self.leaves = {}
        self.end = False 


class WordDictionary:

    def __init__(self):
        self.dictionary = Trie()

    def addWord(self, word: str) -> None:
        node = self.dictionary 
        for c in word:
            if not node.leaves.get(c):
                node.leaves[c] = Trie()
            node = node.leaves[c]
        node.end = True 
            
    def search(self, word: str) -> bool:
        
        def searchnode(idx, node):
            for i in range(idx, len(word)):
                c = word[i]
                if c == '.':
                    for leafnode in node.leaves.values():
                        if searchnode(i+1, leafnode):
                            return True 
                    return False
                else:
                    leafnode = node.leaves.get(c)
                    if not leafnode: 
                        return False
                    node = leafnode 
                    continue 
                    
            return node.end 
            
            
        node = self.dictionary
        return searchnode(0, node)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)