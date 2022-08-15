"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None:
            return None
        
        node = head
        while node:
            new_node = Node(node.val)
            nxt = node.next
            node.next = new_node
            new_node.next = nxt
            node = nxt
        
        node = head
        while node:
            node.next.random = node.random.next if node.random else None 
            node = node.next.next
        
        start, node = head.next, head
        
        while node:
            replica = node.next
            if replica:
                node.next = replica.next
            node = replica
        
        return start
    