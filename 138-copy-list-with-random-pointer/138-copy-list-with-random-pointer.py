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
        node = head
        hm  = {}
        start = None
        
        while node:
            hm[node] = Node(node.val)
            if start is None:
                start = hm[node]
            node = node.next
        
        for old_node, new_node in hm.items():
            new_node.next = hm.get(old_node.next, None)
            new_node.random = hm.get(old_node.random, None)
            
        return start