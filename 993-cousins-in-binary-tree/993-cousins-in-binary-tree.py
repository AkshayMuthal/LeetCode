# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        que = deque()
        que.append(root)
        while que:
            size = len(que)
            xp, yp = False, False
            for i in range(size):
                node = que.popleft()
                if node.val == x:
                    xp = True
                if node.val == y:
                    yp = True
                
                if node.left and node.right:
                    if node.left.val == x and node.right.val == y:
                        return False
                    if node.left.val == y and node.right.val == x:
                        return False
                
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                
            if xp and yp:
                return True
        return False