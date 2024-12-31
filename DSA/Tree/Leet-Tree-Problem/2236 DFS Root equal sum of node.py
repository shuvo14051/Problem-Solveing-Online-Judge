class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

# DFS (pre-order) Approach
class Solution:

    def __init__(self):
        self.li = []

    def checkTree(self, root):
        current = root

        if current is None:
            return self.li
        
        self.li.append(current.val)
        self.checkTree(current.left)
        self.checkTree(current.right)

        return self.li[0] == sum(self.li[1:])
    
root = TreeNode(10)
root.left = TreeNode(4)
root.right = TreeNode(6)

s = Solution()
print(s.checkTree(root))

