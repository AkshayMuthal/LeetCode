# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, l))
        
        head = tail =  ListNode()
        while len(heap)>0:
            val, node = heapq.heappop(heap)
            tail.next = node
            tail = node
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, node))
        
        return head.next
    