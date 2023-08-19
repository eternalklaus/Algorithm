# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# from left to right, *level by level*
# not as simple as simple DFS
# because we should have hint about level of the node. 
class Solution(object):
    output   = []
    nodequeue = []
    nthlevel = []
    level = 0

    def nthlevel2output(self):
        if self.nthlevel: # not empty
            self.output.append(self.nthlevel)
        else:
            pass 
        self.nthlevel = [] # flush same level vars
        
    def levelOrder(self, root):
        # initialize
        self.output = []
        self.nodequeue = []
        self.nthlevel = []
        self.level = 0

        # start from root node
        self.nodequeue.append([root, 0])

        while self.nodequeue: # not empty 
            [node, lvl] = self.nodequeue.pop(0) # left pop
            if node == None:
                continue

            # Update nodequeue
            self.nodequeue.append([node.left , lvl + 1])
            self.nodequeue.append([node.right, lvl + 1])

            # Update nthlevel & output
            if lvl == self.level: # We're still in same level 
                self.nthlevel.append(node.val) 

            else: # We entered into different level! incorporate nthlevel into output!
                self.level = lvl # update level
                self.nthlevel2output()
                self.nthlevel.append(node.val) # append current val
        
        self.nthlevel2output() # last nthlevel : incorporate by itself :] 
        return self.output