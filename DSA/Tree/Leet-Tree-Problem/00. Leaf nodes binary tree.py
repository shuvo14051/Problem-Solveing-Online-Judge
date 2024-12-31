from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root) -> int:
        s = 0
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node.left and not node.right:
                s += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return s