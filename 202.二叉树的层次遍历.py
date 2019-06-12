class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def levelOrder_bfs(self, root: TreeNode) -> list:
        if root ==None:
            return []
        #def bfs(self,root): # 二叉树的层次遍历
        result = []
        queue=[]
        queue.append(root)
        while queue:
            every_layer=[]
            for i in range(len(queue)):
                r=queue.pop(0)
                if  r.left :
                   queue.append(r.left)
                if r.right :
                   queue.append(r.right)
                every_layer.append(r.val)
            print(every_layer)
            result.append(every_layer)
        return result
        #return bfs(self,root)
    def levelOrder_dfs(self, root: TreeNode) -> list:
        if not root:
            return []
        res = []
        levels = 0
        def helper(root:TreeNode,res:list,levels):
            print(levels)
            if len(res) == levels:
                res.append([])
            res[levels].append(root.val)
            if root.left:
                helper(root.left,res,levels+1)
            if root.right:
                helper(root.right,res,levels+1)
        helper(root,res,levels)
        return res
if __name__ =='__main__':
    s=Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(s.levelOrder_dfs(root))