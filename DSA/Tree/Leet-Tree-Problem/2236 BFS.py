class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

# BFS Approach
class Solution:
    def checkTree(self, root):
        li = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            li.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return li[0] == sum(li[1:])

