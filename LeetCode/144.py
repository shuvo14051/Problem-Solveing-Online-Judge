class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.li = []

    def preorderTraversal(self, root):
        current = root
        if current is None:
            return []
        self.li.append(current.val)
        self.preorderTraversal(current.left)
        self.preorderTraversal(current.right)

        return self.li
    
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

s = Solution()
print(s.preorderTraversal(root))

        