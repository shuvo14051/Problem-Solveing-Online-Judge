
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Create the nodes
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

from collections import deque

class Solution:
    def levelOrder(self, root):
      if root is None:
        return []

      results = []
      queue = deque([root])
      while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
          node = queue.popleft()
          current_level.append(node.val)
          if node.left:
            queue.append(node.left)
          if node.right:
            queue.append(node.right)
        results.append(current_level)
      return results
    
s = Solution()
print(s.levelOrder(root))