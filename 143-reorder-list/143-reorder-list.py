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
        # change order? how to make beautiful code?
        nodelist = []
        node = head
        while node:
            nodelist.append(node)
            node = node.next 
        
        orderedlist, L = [], len(nodelist)
        li, ri = 0, L-1
        while li < ri:
            orderedlist.append(nodelist[li])
            orderedlist.append(nodelist[ri])
            li += 1
            ri -= 1
        # append last node 
        if li == ri:
            orderedlist.append(nodelist[li])
        
        i = -1 
        for i in range(L-1):
            orderedlist[i].next = orderedlist[i+1]
        orderedlist[i+1].next = None 
            
            