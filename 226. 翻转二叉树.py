class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root :
            return None
        root.right,root.left=self.invertTree(root.left),self.invertTree(root.right)
        return root

root = TreeNode(4)
root.left=TreeNode(2)
root.right=TreeNode(7)
root.left.left=TreeNode(1)
root.left.right=TreeNode(3)
root.right.left=TreeNode(6)
root.right.right=TreeNode(9)
s=Solution()
s.invertTree(root)

def midTraverse(root:TreeNode):
    if not root:
        return
    midTraverse(root.left)
    print(root.val)
    midTraverse(root.right)

midTraverse(root)