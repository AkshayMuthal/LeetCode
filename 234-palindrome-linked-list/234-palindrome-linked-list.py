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
        slow, fast, prev = head, head, None
        
        while fast and fast.next:
            fast = fast.next.next
            
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        if fast:
            slow = slow.next
        
        head = slow
        rev_head = prev
        
        # compare
        while head and rev_head:
            if head.val != rev_head.val:
                return False
            head = head.next
            rev_head = rev_head.next
        
        return True