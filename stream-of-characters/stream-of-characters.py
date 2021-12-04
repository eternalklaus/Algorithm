class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {} # reversed trie
        self.string = ''
        
        for word in words:
            node = self.trie    
            for ch in word[::-1]:
                if ch not in node: # if char isnt in node, 
                    node[ch] = {} 
                node = node[ch] # move to next level 
            node['END'] = True # check the endpoint
                
                
    def query(self, letter: str) -> bool:
        self.string = letter + self.string 
        # print (self.string)
        node = self.trie
        for ch in self.string:
            if 'END' in node: return True 
            if ch not in node: return False 
            node = node[ch]
        
        return 'END' in node
            
            


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)