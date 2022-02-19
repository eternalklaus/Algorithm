"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        investigated = set()
        nodedict = {}
        queue = [node]
        
        def getnode(val): # return val node, if not exist, creat it
            if val not in nodedict:
                nodedict[val] = Node(val)
            return nodedict[val] 
        
        while queue: # queue follows original node
            node = queue.pop(0) 
            if not node: 
                continue # empty node
            if node in investigated: # already investigated the relationship between neighbors. skip it. 
                continue 
                
            investigated.add(node) # add into investigared
            
            clone_node = getnode(node.val)
            for neighbor in node.neighbors: 
                queue.append(neighbor)
                clone_neighbor = getnode(neighbor.val)
                clone_node.neighbors.append(clone_neighbor) 
        
                
        return nodedict.get(1)
        