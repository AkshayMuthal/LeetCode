# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def cycle(self, curr, nxt):
        if curr == None or nxt == None or nxt.next == None:
            return False
        if curr == nxt:
            return True
        curr = curr.next
        nxt = nxt.next.next
        return self.cycle(curr, nxt)
        
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        return self.cycle(head, head.next)
        