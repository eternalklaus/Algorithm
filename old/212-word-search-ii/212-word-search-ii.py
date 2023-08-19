class Trie:
    import string 
    def __init__(self): ###<=
        self.char = {}
        self.end = False 
        
    
class Solution:
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        output = []
        root = Trie()
        for word in words:
            node = root 
            for c in word:
                if not node.char.get(c):
                    node.char[c] = Trie() 
                node = node.char[c]
            node.end = word ###<-!!! 
        
        def search(i, j, node):
            nonlocal output 
            # base case 
            if not 0<=i<len(board): return  
            if not 0<=j<len(board[0]): return  

            c = board[i][j]
            childnode = node.char.get(c)
            if not childnode: return  

            if childnode.end: # exist end!
                output.append(childnode.end)
                childnode.end = False 
                if not childnode.char: ###
                    del node.char[c]

            board[i][j] = '$' 
            search(i+1, j, childnode)
            search(i-1, j, childnode)
            search(i, j+1, childnode)
            search(i, j-1, childnode) 
            board[i][j] = c
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                search(i, j, root)
        return output

