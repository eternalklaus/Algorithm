class Solution(object):
    def getdepth(self, node):
        if node == None:
            return 0 
        lchild = node.left 
        rchild = node.right
        
        ldepth = 1 + self.getdepth(lchild)
        rdepth = 1 + self.getdepth(rchild)
        max(ldepth, rdepth)

    def maxDepth(self, root):
        return self.getdepth(root) 
        