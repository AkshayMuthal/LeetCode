# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        
        q = deque()
        max_r = -10000
        
        while root:
            max_r = max(max_r, root.val)
            q.append((root, max_r))
            if root.val>=max_r:
                self.count+=1
            root = root.left
        
        while len(q)>0:
            elem, max_r = q.pop()
            elem = elem.right
            
            while elem:
                max_r = max(max_r, elem.val)
                q.append((elem, max_r))
                if elem.val>=max_r:
                    self.count+=1
                elem = elem.left
            
        return self.count