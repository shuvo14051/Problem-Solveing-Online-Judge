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