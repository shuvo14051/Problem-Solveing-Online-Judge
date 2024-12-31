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
        result = []

        while queue:
            result = []
            for _ in range (len(queue)):
                node = queue.popleft()
                result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

root.left.left.left = TreeNode(7)
root.right.right.right = TreeNode(8)

s =   Solution()
print(s.deepestLeavesSum(root))
        



