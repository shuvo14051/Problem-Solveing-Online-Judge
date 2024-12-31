from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

# Create the second tree: q = [1,2,3]
q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

# Create an instance of the Solution class
solution = Solution()

# Call the isSameTree method
result = solution.isSameTree(p, q)

print(f"{result}")
