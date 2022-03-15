"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        nodedict = {None:None}
        
        def dfs(node): 
            if node in nodedict: return nodedict[node] # including None 
            
            newnode = Node(node.val)
            nodedict[node] = newnode # register it 
            
            for neighbor in node.neighbors: 
                newnode.neighbors.append(dfs(neighbor))
            
            return newnode
            
        return dfs(node)