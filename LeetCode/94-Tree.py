# Definition for a binary tree node.
from typing import List 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
       
class Solution:
    def __init__(self):
        self.li = []

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        self.inorderTraversal(root.left)
        self.li.append(root.val)
        self.inorderTraversal(root.right)
        return self.li
        