# Definition for a binary tree node.层次遍历，比较是否对称
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = []
        queue.append(root)
        while queue:
            every_level = []
            for i in range(len(queue)):
                tem = queue.pop(0)
                if tem == None:
                    every_level.append(None)
                    continue
                every_level.append(tem.val)
                queue.append(tem.left)
                queue.append(tem.right)
            print(every_level)
            for i in range(len(every_level)//2):
                if every_level[i] != every_level[len(every_level)-1-i]:
                    return False
        return True
root = TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(2)
root.left.left=TreeNode(3)
#root.left.right=TreeNode(4)
root.right.left=TreeNode(4)
#root.right.right=TreeNode(3)
s=Solution()
print(s.isSymmetric(root))