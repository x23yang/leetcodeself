class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def __init__(self):
    #     self.res = []
    def maxLevels(self,root:TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxLevels(root.left)+1,self.maxLevels(root.right)+1)
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        #self.res.append(self.maxLevels(root.left)+self.maxLevels(root.right))
        t1 =self.maxLevels(root.left)+self.maxLevels(root.right)
        t2 = self.diameterOfBinaryTree(root.left)
        t3 = self.diameterOfBinaryTree(root.right)
        return max(t1,t2,t3)
root = TreeNode(4)
root.left=TreeNode(2)
root.right=TreeNode(7)
root.left.left=TreeNode(1)
root.left.right=TreeNode(3)
root.right.left=TreeNode(6)
root.right.right=TreeNode(9)
s=Solution()
print(s.diameterOfBinaryTree(root))