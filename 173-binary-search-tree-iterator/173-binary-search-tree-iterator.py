# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.nodes = []
        self.add_elem(root)
        
    def add_elem(self, node):
        while node:
            self.nodes.append(node)
            node = node.left
            
    def next(self) -> int:
        elem = self.nodes.pop()
        if elem.right:
            self.add_elem(elem.right)
        return elem.val

    def hasNext(self) -> bool:
        if len(self.nodes)>0:
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()