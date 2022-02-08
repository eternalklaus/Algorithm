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
        
        def prunechild(node): # cut dead branch(has no 'end')
            if node.end: return False 
            # if there's no accumulated 'end', this branch is dealt as dead branch 
            if not node.char: return True 

            no_end_in_this_tree = True 
            for c in node.char:
                if prunechild(node.char[c]):
                    del node.char[c]
                else: 
                    no_end_in_this_tree = False 
            return no_end_in_this_tree
                
        def search(i, j, node):
            nonlocal output 
            # base case 
            if not 0<=i<len(board): return False
            if not 0<=j<len(board[0]): return  False

            c = board[i][j]
            childnode = node.char.get(c)
            if not childnode: return  False

            if childnode.end: # exist end!
                output.append(childnode.end)
                childnode.end = False 
            
            res = False 
            board[i][j] = '$' 
            res |= search(i+1, j, childnode)
            res |= search(i-1, j, childnode)
            res |= search(i, j+1, childnode)
            res |= search(i, j-1, childnode) 
            board[i][j] = c
            
            if res:
                prunechild(node)
            return res 

        for i in range(len(board)):
            for j in range(len(board[0])):
                search(i, j, root)
        return output

