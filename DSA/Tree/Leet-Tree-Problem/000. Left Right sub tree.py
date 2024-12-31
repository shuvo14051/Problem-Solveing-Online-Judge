from collections import deque

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.right = None
		self.left = None

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

class Solution:
	def bfs(self, root):
		if root is None:
			return True

		li = []
		queue = deque([root])

		while queue:
			node = queue.popleft()
			li.append(node.val)

			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)

		return li

	def isSymmetric(self):
		l_sub_tree = bfs(root.left)
		r_sub_tree = bfs(root.right)

		return l_sub_tree, r_sub_tree

s = Solution()
print(s.check_Mirror())
