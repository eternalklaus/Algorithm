"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        nodelist = []
        
        def connectnode(nodelist):
            for i in range(1, len(nodelist) - 1):
                lnode = nodelist[i - 1]
                cnode = nodelist[i]
                rnode = nodelist[i + 1]

                cnode.prev = lnode
                cnode.next = rnode
                
                lnode.next = cnode
                rnode.prev = cnode

                cnode.child = None # <- This is nessesary..-_-
            
            if len(nodelist) > 0:
                nodelist[0].prev = None 
                nodelist[0].child = None 

                nodelist[len(nodelist) - 1].next = None 
                nodelist[len(nodelist) - 1].child = None 

        def dfs(node):
            if not node: 
                return 
            nodelist.append(node)
            if node.child:
                dfs(node.child)
            if node.next:
                dfs(node.next)
            else:
                return

        dfs(head)
        connectnode(nodelist)
        '''
        for node in nodelist:
            if node.prev == None:
                lval = -1
            elif node.prev != None: 
                lval = node.prev.val 
            if node.next == None: 
                rval = -1
            elif node.next != None: 
                rval = node.next.val 
            print "%d <- %d -> %d" % (lval, node.val, rval)
        '''
        return head