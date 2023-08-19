
from collections import defaultdict
class Node:
    def __init__(self): # is it nessasary?
        self.child = {} #naming. not char but child
        self.end = False 

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root 
        for c in word:
            if c not in node.child:
                node.child[c] = Node()
            node = node.child[c]
        node.end = True

    def search(self, word: str) -> bool:
        node = self.root 
        for c in word:
            if c not in node.child:
                return False 
            node = node.child[c]
        if node.end == True:
            return True 
        else:
            return False 
        
    def startsWith(self, prefix: str) -> bool:
        node = self.root 
        for c in prefix:
            if c not in node.child:
                return False 
            node = node.child[c]
        return True
