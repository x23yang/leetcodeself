class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def Count(root: TreeNode) -> int:
            if not root:
                return 0
            return Count(root.left)+Count(root.right)+1
        # if not root :
        #     if k == 1:
        #         return root 
        leftCount = Count(root.left)
        if leftCount == k-1:
            return root.val 
        elif leftCount > k-1:
            return self.kthSmallest(root.left,k)
        else:
            return self.kthSmallest(root.right,k-leftCount-1)

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)
s=Solution()
temp = s.kthSmallest(root,3)
print(temp)