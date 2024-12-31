from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        s = 0
        queue = deque([root])
        while queue:
            node = queue.popleft()
            data = node.val
            if data>= low and data<=high:
                s+=data
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return s

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)

s = Solution()
print(s.rangeSumBST(root, 7, 15))
