# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head.next        
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse
        prev = None
        rev_head = slow.next
        slow.next = None
        while rev_head:
            nxt = rev_head.next
            rev_head.next = prev
            prev = rev_head
            rev_head = nxt
            
        rev_head = prev
        
        # compare
        while head and rev_head:
            if head.val != rev_head.val:
                return False
            head = head.next
            rev_head = rev_head.next
        
        return True