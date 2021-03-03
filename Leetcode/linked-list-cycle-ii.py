# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    cache = set()

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head 
        
        while True:
            ### case 1: cycle not exist
            if node == None: 
                return None 
            
            ### case 2: found circle!
            if node in self.cache:
                return node
            
            self.cache.add(node)
            node = node.next 
