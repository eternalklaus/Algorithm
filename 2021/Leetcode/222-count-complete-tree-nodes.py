class Solution(object):
    def calclevel(self, node):
        lnode = node 
        rnode = node 
        llevel = 0
        rlevel = 0
        while lnode: 
            lnode = lnode.left 
            llevel += 1
        while rnode:
            rnode = rnode.right
            rlevel += 1
        
        return llevel, rlevel
        

    def countNodes(self, root):
        totallevel, _ = self.calclevel(root) 
        node = root 
        lastnodenum = 2 ** (totallevel - 1) # 
        lastnodenum_base = 0
        lastnodenum_top = lastnodenum
        while node:
            lllevel, lrlevel = self.calclevel(node.left)
            rllevel, rrlevel = self.calclevel(node.right)
            
            if lllevel > lrlevel:
                node = node.left 
                lastnodenum_top = (lastnodenum_base + lastnodenum_top) / 2
            elif rllevel > rrlevel:
                node = node.right 
                lastnodenum_base = (lastnodenum_base + lastnodenum_top) / 2
            elif lrlevel > rllevel:
                lastnodenum = lastnodenum_base + (lastnodenum_top - lastnodenum_base)/2
                break 
            elif lllevel == rrlevel:
                lastnodenum = lastnodenum_top # This subtree is complete tree
                break 
        
        
        totalnodenum = (2 ** (totallevel - 1) - 1) + lastnodenum
        
        return int(totalnodenum)