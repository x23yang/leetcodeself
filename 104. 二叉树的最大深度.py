# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        elif root.left == None and root.right ==None:
            return 1
        a = self.maxDepth(root.left)+1
        b = self.maxDepth(root.right)+1
        return max(a,b)
