# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverse(self, node):
        prev = None
        while node:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
        return prev
    
    
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        start, node = head, ListNode(0)
        end = self.reverse(slow.next)
        
        slow.next = None
        
        while start and end:
            node.next = start
            start = start.next
            node = node.next
            
            node.next = end
            end = end.next
            node = node.next
        
        if start:
            node.next = start
        
        return head