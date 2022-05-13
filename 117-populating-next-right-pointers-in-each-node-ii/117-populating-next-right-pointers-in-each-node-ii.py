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
        if root == None:
            return None
        
        queue = deque()
        queue.append(root)
        nxt = None
        while len(queue)>0:
            l = len(queue)
            while l>0:
                elem = queue.pop()
                if elem.right!=None:
                    queue.appendleft(elem.right)
                if elem.left!=None:
                    queue.appendleft(elem.left)
                elem.next = nxt
                nxt = elem
                l-=1
            nxt = None
        return root
