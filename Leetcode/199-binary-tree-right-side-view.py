class Solution(object):
    nextlevelQ = []
    thislevelQ = []
    output = []
    
    def rightSideView(self, root):
        ### Flush caches for reusing the code
        self.nextlevelQ = []
        self.thislevelQ = []
        self.output = []

        ### Initialize Queue 
        if root is not None:
            self.nextlevelQ.append(root) # <= Exception handling 1: the case of node == None
        
        while self.nextlevelQ:
            self.thislevelQ = self.nextlevelQ
            self.nextlevelQ = [] # <= do not forget to initialize it!
            
            while self.thislevelQ:
                node = self.thislevelQ.pop(0)
                
                if self.thislevelQ == []: # this node is the last node 
                    self.output.append(node.val)
                if node.left: # Execption handling 2
                    self.nextlevelQ.append(node.left)
                if node.right: # Execption handling 3
                    self.nextlevelQ.append(node.right)
        
        return self.output
