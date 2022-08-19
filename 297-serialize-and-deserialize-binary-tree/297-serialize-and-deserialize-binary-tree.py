# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return "-1002"
        level = deque()
        level.append(root)
        ans = []
        
        while level:
            level_len = len(level)
            
            for i in range(level_len):
                elem = level.popleft()
                ans.append(elem.val if elem else -1002)
                if elem:
                    level.append(elem.left)
                    level.append(elem.right)
        
        ans = ",".join([str(i) for i in ans])
        return ans
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = [int(i) for i in data.split(",")]
        if data[0] == -1002:
            return None
        ind = 0
        level = deque()
        level.append(TreeNode(data[0]))
        head = level[0]
        
        while level:
            len_level = len(level)
            for i in range(len_level):
                node = level.popleft()
                if node:
                    if ind+1<len(data):
                        ind += 1
                        node.left = TreeNode(data[ind]) if data[ind]!=-1002 else None
                        level.append(node.left)
                    if ind+1<len(data):
                        ind += 1
                        node.right = TreeNode(data[ind]) if data[ind]!=-1002 else None
                        level.append(node.right)
        return head
                
            
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))