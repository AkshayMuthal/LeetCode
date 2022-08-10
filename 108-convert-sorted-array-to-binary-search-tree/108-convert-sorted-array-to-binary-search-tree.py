# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def get_root(self, arr, l, r):
        if l>r:
            return None
        mid = l+(r-l)/2
        node = TreeNode(arr[mid])
        node.left = self.get_root(arr, l, mid-1)
        node.right = self.get_root(arr, mid+1, r)
        return node
    
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.get_root(nums, 0, len(nums)-1)