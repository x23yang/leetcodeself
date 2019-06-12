class TreeNode:
    def __init__(self,val,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right
def preTraverse(root:TreeNode):
    if not root:
        return
    print(root.val)
    preTraverse(root.left)
    preTraverse(root.right)

def midTraverse(root:TreeNode):
    if not root:
        return
    midTraverse(root.left)
    print(root.val)
    midTraverse(root.right)

def postTraverse(root:TreeNode):
    if not root:
        return
    postTraverse(root.left)
    postTraverse(root.right)
    print(root.val)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

preTraverse(root)
print('------')
midTraverse(root)
print('------')
postTraverse(root)