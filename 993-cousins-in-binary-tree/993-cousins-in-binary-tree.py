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
        self.yd, self.xd, self.xp, self.yp = 0, 0, None, None
        
        def height(node, parent, yd, xd):
            if node != None:
                if self.xp!=None and self.yp!=None:
                    return
                if node.val == x:
                    self.xd = xd
                    self.xp = parent
                if node.val == y:
                    self.yd = yd
                    self.yp = parent
                height(node.left, node, yd+1, xd+1)
                height(node.right, node, yd+1, xd+1)
        
        height(root, None, 0, 0)
        
        return True if self.xd == self.yd and self.xp != self.yp else False