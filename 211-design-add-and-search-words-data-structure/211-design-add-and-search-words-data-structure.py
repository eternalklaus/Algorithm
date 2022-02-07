class Trie:
    def __init__(self):
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
        queue = [self.dictionary, 'QEND']
        for c in word:
            if not queue: 
                return False 
            
            while queue:
                node = queue.pop(0)
                if not node: continue
                if node == 'QEND': break 
                
                if c == '.':
                    nextnodes = list(node.leaves.values())
                    queue += nextnodes 
                else:
                    queue.append(node.leaves.get(c)) # append regardless node is None or not 
            queue.append('QEND')
            
        while queue:
            node = queue.pop(0)
            if not node: continue 
            if node == 'QEND': break 
            if node.end: return True
        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)