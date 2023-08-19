# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tortoise = head 
        hare = head 

        while True:
            ### 0st exception handling 
            if head == None:
                return None 

            ### Move and 1st exception handling 
            tortoise = tortoise.next 
            hare = hare.next 
            if tortoise == None or hare == None: return None 
            
            ### Move and 2nd exception handling 
            hare = hare.next 
            if hare == None: return None 

            ### They finally meet!
            if tortoise == hare: 
                break 
        
        ### get meeting spot 
        intersect   = tortoise 
        node        = head # walk from first node 

        while True:
            if intersect == node:
                return node 
            ### We don't need exception handling since the existence of circle is already proved at above. 
            intersect = intersect.next 
            node = node.next 

