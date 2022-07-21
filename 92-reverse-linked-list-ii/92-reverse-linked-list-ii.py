# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        root = head
        
        rev_head_par = None
        curr = 1
        
        while head!=None and curr!=left:
            rev_head_par = head
            head = head.next
            curr += 1
        
        prev = rev_head_par
        if rev_head_par:
            rev_head_par.next = None
        rev_head = head
        
        
        while head!=None and curr!=right+1:
            # print("B: ", head.val)
            temp = head.next
            head.next = prev
            prev = head
            head = temp
            curr += 1
            # print("A: ", head)
            
        # print(head)
        
        rev_head.next = head
        if rev_head_par:
            rev_head_par.next = prev
        
        return root if left!=1 else prev
        