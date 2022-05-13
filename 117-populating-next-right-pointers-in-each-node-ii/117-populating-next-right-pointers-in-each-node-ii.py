"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        curr = root
        head = None
        prev = None
        while curr!=None:
            while curr != None:
                if curr.left != None:
                    if prev != None:
                        prev.next = curr.left
                    else:
                        head = curr.left
                    prev = curr.left
                if curr.right != None:
                    if prev != None:
                        prev.next = curr.right
                    else:
                        head = curr.right
                    prev = curr.right
                curr = curr.next
            curr = head
            prev = None
            head = None
        return root
