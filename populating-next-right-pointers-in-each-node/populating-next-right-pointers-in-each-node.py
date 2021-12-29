"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# Lets catch bugs!!!
# BFS 
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = [root, None]
        
        while queue:
            node = queue.pop(0)
            
            if node:
                # print (node.val)
                queue.append(node.left)
                queue.append(node.right) 
                node.next = queue[0]
            else:
                # print (node)
                queue.append(None)
                setqueue = set(queue)
                if setqueue.pop() == None and not setqueue: # only None(s) are left
                    break 
                
        return root