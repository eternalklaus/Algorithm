
class Trie:

    def __init__(self):
        self.dictionary = {}

    def insert(self, word: str) -> None:
        node = self.dictionary 
        for c in word:
            if not node.get(c): 
                node[c] = {} # assign new dict leaf 
            node = node[c] # move down 
        node['END'] = True 
        
    def search(self, word: str) -> bool:
        node = self.dictionary 
        for c in word:
            if not node.get(c): return False 
            node = node[c]
        if node.get('END'): return True 
        return False 

    def startsWith(self, prefix: str) -> bool:
        node = self.dictionary 
        for c in prefix:
            if not node.get(c): 
                return False 
            node = node[c]
        return True 
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)