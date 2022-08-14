# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        node, prev = head, None
        while node:
            if node.val == val:
                if prev == None:
                    head = node.next
                else:
                    prev.next = node.next
            else:
                prev = node
            node = node.next
        return head