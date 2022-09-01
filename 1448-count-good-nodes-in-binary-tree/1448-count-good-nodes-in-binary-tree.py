# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count, max_val = 0, root.val
        q = deque()
        
        node = TreeNode()
        node.right = root
        q.append((node, max_val))
        
        while len(q)>0:
            node, max_val = q.pop()
            node = node.right
            
            while node:
                max_val = max(node.val, max_val)
                q.append((node, max_val))
                if node.val >= max_val:
                    count += 1
                node = node.left
        
        return count
            