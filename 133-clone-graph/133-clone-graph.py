"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        ### cannot solved with dfs since circle exist (function not returns)
        if not node: 
            return None 
        
        root = node 
        visited = {node:Node(node.val)}
        queue = [node]
        
        while queue:
            node = queue.pop(0)
            clone = visited[node]
            
            # it already checked visited in previous cycle 
            for neighbor in node.neighbors:
                if neighbor in visited: 
                    cloneneighbor = visited[neighbor]
                else:
                    cloneneighbor = Node(neighbor.val)
                    queue.append(neighbor) # go complete neighbor relational graph for neighbor
                    visited[neighbor] = cloneneighbor # mark as visited 
                
                clone.neighbors.append(visited[neighbor])
                
        return visited[root]