# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reversenode(self, head, num):
        prevnode = None # TODO 
        node = head

        for i in xrange(num - 1):
            nextnode = node.nextπ
            node.next = prevnode

            # setting for next for loop
            prevnode = node
            node = nextnode

        return prevnode, head, nextnode



    def reverseBetween(self, head, m, n):
        node = head 
        for i in xrange(m):
            node= node.next

        _revhead, _revtail, _restnodes = self.reversenode(node, n - m + 1)
        
        node.next = _revhead
        _revtail.next = _restnodes

        return head
            