# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 1. Make it linked list -> list
        nodes, node = [], head 
        while node:
            nodes.append(node)
            node = node.next 
        
        # 2. Order list
        ordered, L = [], len(nodes)
        li, ri = 0, L-1
        while li < ri:
            ordered.append(nodes[li])
            ordered.append(nodes[ri])
            li += 1
            ri -= 1
        # 2.2 append last node 
        if li == ri:
            ordered.append(nodes[li])
        
        # 3. Reconnect nodes
        i = -1 
        for i in range(L-1):
            ordered[i].next = ordered[i+1]
        ordered[i+1].next = None 
            
            