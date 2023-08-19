class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        class Trie():
            def __init__(self, char):
                self.char = char
                self.counter = 0
                self.children = {}
            
        
        root = Trie('')
        for word in words:
            # register in trie
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = Trie(c)
                node = node.children[c]
                node.counter += 1
                
        output = []
        for word in words:
            # count the children of each tri nodes...
            counter, node = 0, root
            for c in word:
                node = node.children[c]
                counter += node.counter 
            output.append(counter)
        return output
            
            