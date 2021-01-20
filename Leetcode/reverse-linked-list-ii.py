# https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseBetween(self, head, m, n):
        m = m-1
        n = n-1

        def changenum(left, li, ri):
            # set node1
            node1 = left 
            node2 = None 
            movenum = ri - li

            # get node2
            node = node1 
            for i in xrange(movenum):
                node = node.next
            node2 = node
            
            # swap
            tmp = node1.val 
            node1.val = node2.val 
            node2.val = tmp 
        
        # move node until the very first swap node
        left = head 
        for i in xrange(m):
            left = left.next 

        for i in range(m, n):
            li = i 
            ri = (m + n) - li 
            if li >= ri: break 

            changenum(left, li, ri)
            left = left.next

        return head 
        