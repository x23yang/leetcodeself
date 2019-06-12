class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        t1 = root.left
        t2 = root.right
        #判断两棵树是否为镜像
        def helper(t1,t2) ->bool:
            if t1 ==None and t2 ==None:
                return True
            if t1 == None and t2 !=None:
                return False
            if t1 != None and t2 ==None:
                return False
            if t1.val == t2.val:
                return helper(t1.left,t2.right) and helper(t1.right,t2.left)
            else:
                return False
        return helper(t1,t2)
root = TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(2)
root.left.left=TreeNode(3)
root.left.right=TreeNode(4)
root.right.left=TreeNode(4)
root.right.right=TreeNode(3)
s=Solution()
print(s.isSymmetric(root))


