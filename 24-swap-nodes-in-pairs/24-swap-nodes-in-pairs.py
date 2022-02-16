# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        pre = head
        nxt = head.next
        
        while pre!=None and nxt!=None:
            temp = pre.val
            pre.val = nxt.val
            nxt.val = temp
            pre = nxt.next
            if pre is not None:
                nxt = pre.next
            else:
                nxt = None
        
        return head
        