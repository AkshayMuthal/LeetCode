# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check_pallindrome(queue):
            l, r = 0, len(queue)-1
            while l<r:
                if queue[l] == None and queue[r] == None:
                    l+=1
                    r-=1
                    continue
                if (queue[l] and queue[r] == None) or (queue[r] and queue[l] == None) or (queue[l].val!=queue[r].val):
                    return False
                l+=1
                r-=1
            return True
        
        queue = deque()
        queue.append(root)
        
        while queue:
            l = len(queue)
            if not check_pallindrome(queue):
                return False
            for i in range(l):
                elem = queue.popleft()
                if elem!=None:
                    queue.append(elem.left)
                    queue.append(elem.right)
        return True