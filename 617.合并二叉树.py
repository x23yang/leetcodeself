# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode,t1_p=None,t2_LR=None) -> TreeNode:
        if t1 == None and t2 == None:
            return None
        if t1 == None and t2 != None:
            # if t1_p== None:
            #     return t2
            # if t2_LR==0:
            #     t1_p.left = t2
            # if t2_LR==1:
            #     t1_p.right = t2
            t1 = t2
            return t1
        if t1 != None and t2 == None:
            return t1
        if t1 and t2 :
            t1.val = t1.val +t2.val
            t1.left = self.mergeTrees(t1.left,t2.left,t1_p=t1,t2_LR=0)
            t1.right = self.mergeTrees(t1.right,t2.right,t1_p=t1,t2_LR=1)
            return t1

        # if t1 and t2 :
        #     t1.val += t2.val
        #     t1.left = self.mergeTrees(t1.left, t2.left)
        #     t1.right = self.mergeTrees(t1.right, t2.right)
        #     return t1
        # return t1 or t2

t1 = TreeNode(1)
t1.left=TreeNode(3)
t1.right = TreeNode(2)
t1.left.left = TreeNode(5)

t2 = TreeNode(2)
t2.left=TreeNode(1)
t2.right=TreeNode(3)
t2.left.right= TreeNode(4)
t2.right.right=TreeNode(7)
s=Solution()
s.mergeTrees(t1,t2)

def levelOrder_bfs( root: TreeNode) -> list:
    if root == None:
        return []
    # def bfs(self,root): # 二叉树的层次遍历
    result = []
    queue = []
    queue.append(root)
    while queue:
        every_layer = []
        for i in range(len(queue)):
            r = queue.pop(0)
            if r.left:
                queue.append(r.left)
            if r.right:
                queue.append(r.right)
            every_layer.append(r.val)
        print(every_layer)
        result.append(every_layer)
    return result
levelOrder_bfs(t1)




