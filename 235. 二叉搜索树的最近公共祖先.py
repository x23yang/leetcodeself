class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val <= root.val <= q.val or q.val <= root.val <= p.val :
            return root
        if p.val <root.val and q.val <root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        if p.val >root.val and q.val >root.val:
            return self.lowestCommonAncestor(root.right,p,q)
root=TreeNode(6)
root.left=TreeNode(2)
root.right=TreeNode(8)
root.left.left=TreeNode(0)
root.left.right=TreeNode(4)
root.right.left=TreeNode(7)
root.right.right=TreeNode(9)
s=Solution()
temp = s.lowestCommonAncestor(root,root,root.right.right)

def midTraverse(root:TreeNode):
    if not root:
        return
    midTraverse(root.left)
    print(root.val)
    midTraverse(root.right)

midTraverse(temp)

