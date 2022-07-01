# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        
        ans = []
        q = deque()
        q.append(root)
        
        while len(q):
            cl = len(q)
            level_nodes = []
            for i in range(cl):
                elem = q.popleft()
                level_nodes.append(elem.val)
                if elem.left!=None:
                    q.append(elem.left)
                if elem.right!=None:
                    q.append(elem.right)
            ans.append(level_nodes)
        
        return ans
            